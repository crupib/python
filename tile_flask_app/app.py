from flask import Flask, render_template, abort, send_from_directory, jsonify, request, redirect, url_for, flash, make_response
import os, socket, subprocess, platform, glob, shutil, sys, shlex, threading, time

from werkzeug.utils import secure_filename

# External tiles require PyYAML to read config/functions.d/*.y*ml
try:
    import yaml
except Exception:
    yaml = None

app = Flask(__name__)
app.secret_key = "dev"

# ---------------- System info / favicon ----------------
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon'
    )

@app.context_processor
def inject_system_info():
    system = platform.system()
    os_name = {"Darwin": "macOS", "Linux": "Linux", "Windows": "Windows"}.get(system, system or "Unknown")
    os_version = platform.release()
    hostname = socket.gethostname()
    ip_address = "Unknown"
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        s.close()
    except Exception:
        pass
    return {"hostname": hostname, "os_info": f"{os_name} {os_version}", "ip_address": ip_address}

# ---------------- Built-in tiles ----------------
BUILTIN_FUNCTIONS = [
    {"slug": "settings",  "title": "Settings",  "description": "Configure system options and preferences", "options": []},
    {"slug": "functions", "title": "Functions", "description": "System utilities and network tools",       "options": []},
    {"slug": "help",      "title": "Help",      "description": "Diagnostics and service controls",         "options": []},
]

# ---------------- External tiles (Ansible-managed) ----------------
FUNCTIONS_DIR = os.environ.get(
    "NTS_FUNCTIONS_DIR",
    os.path.join(os.path.dirname(__file__), "config", "functions.d")
)
os.makedirs(FUNCTIONS_DIR, exist_ok=True)

_functions_cache = {"mtime": 0.0, "merged": BUILTIN_FUNCTIONS[:]}

def _validate_tile(d: dict) -> bool:
    if not isinstance(d, dict):
        return False
    for key in ("slug", "title", "description"):
        if key not in d or not isinstance(d[key], str) or not d[key].strip():
            return False
    if "options" in d and not isinstance(d["options"], list):
        return False
    return True

def _merge_tiles(builtin, externals):
    by_slug = {b["slug"]: b for b in builtin}
    for e in externals:
        by_slug[e["slug"]] = e
    merged = [by_slug[b["slug"]] for b in builtin]
    for s, t in by_slug.items():
        if s not in {b["slug"] for b in builtin}:
            merged.append(t)
    return merged

def _current_tree_mtime(path):
    try:
        mtimes = [os.path.getmtime(path)]
        for p in glob.glob(os.path.join(path, "*")):
            mtimes.append(os.path.getmtime(p))
        return max(mtimes)
    except Exception:
        return 0.0

def _load_external_tiles():
    tiles = []
    if yaml is None:
        print("[WARN] PyYAML not installed; skipping external tiles")
        return tiles
    for path in glob.glob(os.path.join(FUNCTIONS_DIR, "*.y*ml")):
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
            if not data:
                continue
            candidates = [data] if isinstance(data, dict) else data if isinstance(data, list) else []
            for t in candidates:
                if not _validate_tile(t):
                    print(f"[WARN] Invalid tile in {path}: {t}")
                    continue
                t.setdefault("options", [])
                t.setdefault("bg_color", "#8B0000")
                t.setdefault("image", "images/75th_main.jpeg")
                tiles.append(t)
        except Exception as e:
            print(f"[WARN] Failed to load {path}: {e}")
    return tiles

def _reload_if_changed():
    mtime = _current_tree_mtime(FUNCTIONS_DIR)
    if mtime > _functions_cache["mtime"]:
        externals = _load_external_tiles()
        merged = _merge_tiles(BUILTIN_FUNCTIONS, externals)
        _functions_cache["merged"] = merged
        _functions_cache["mtime"] = mtime
        print(f"[INFO] Reloaded function tiles: builtin={len(BUILTIN_FUNCTIONS)}, external={len(merged)-len(BUILTIN_FUNCTIONS)}")

def get_all_functions():
    _reload_if_changed()
    return _functions_cache["merged"]

def get_function(slug: str):
    for f in get_all_functions():
        if f.get("slug") == slug:
            return f
    return None

# ---------------- Per-OS command runners ----------------
def run_command_for_os(commands_dict):
    sysname = platform.system()  # strict equality
    if sysname == "Darwin":
        key = "macos"
    elif sysname == "Windows":
        key = "windows"
    else:
        key = "linux"
    cmd = commands_dict.get(key)
    if not cmd:
        return f"No command defined for {key}."
    try:
        result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode != 0:
            stderr = (result.stderr or "").strip()
            return f"[ERROR] Command exited {result.returncode}\n{stderr}"
        return (result.stdout or "").strip() or "(no output)"
    except Exception as e:
        return f"[EXCEPTION] {e}"

def run_command_template_for_os(template_dict, form_data: dict):
    sysname = platform.system()
    if sysname == "Darwin":
        key = "macos"
    elif sysname == "Windows":
        key = "windows"
    else:
        key = "linux"

    tmpl = template_dict.get(key)
    if not tmpl:
        return f"No command_template defined for {key}."

    prompt = form_data.get("prompt", "")
    model = form_data.get("model", "")

    ctx = {
        "prompt": prompt,
        "model": model,
        "prompt_sh": shlex.quote(prompt),
        "model_sh": shlex.quote(model),
    }

    try:
        cmd = tmpl.format(**ctx)
    except Exception as e:
        return f"[TEMPLATE ERROR] {e}"

    try:
        result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode != 0:
            stderr = (result.stderr or "").strip()
            return f"[ERROR] Command exited {result.returncode}\n{stderr}"
        return (result.stdout or "").strip() or "(no output)"
    except Exception as e:
        return f"[EXCEPTION] {e}"

# ---------------- Helpers ----------------
def _normalize_form_option(opt: dict) -> dict:
    new_opt = dict(opt or {})
    has_template = bool(new_opt.get("command_template"))
    form = new_opt.get("form") if isinstance(new_opt.get("form"), dict) else None
    fields = (form or {}).get("fields")
    if not (isinstance(fields, list) and fields):
        if has_template:
            new_opt["form"] = {
                "fields": [
                    {"name": "model", "label": "Model", "type": "text", "default": "llama3", "required": True, "placeholder": "llama3"},
                    {"name": "prompt", "label": "Prompt", "type": "textarea", "required": True, "rows": 5, "placeholder": "Type your prompt…"},
                ]
            }
    return new_opt

# ---------------- Service state: VPN + Share + TAK + RallyPoint + Engagebridged + Compass ----------------
VPN_STATE   = {"state": "down"}   # black/down | starting(yellow) | up(green) | error(red)
VPN_LOCK    = threading.Lock()

SHARE_STATE = {"state": "down"}
SHARE_LOCK  = threading.Lock()

TAK_STATE   = {"state": "down"}
TAK_LOCK    = threading.Lock()

RALLY_STATE = {"state": "down"}
RALLY_LOCK  = threading.Lock()

ENGAGEBRIDGED_STATE = {"state": "down"}
ENGAGEBRIDGED_LOCK  = threading.Lock()

COMPASS_STATE = {"state": "down"}
COMPASS_LOCK  = threading.Lock()

def _net_ok():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(1.5)
        s.connect(("1.1.1.1", 53))
        s.close()
        return True
    except Exception:
        return False

def _vpn_restart_worker():
    time.sleep(0.8)
    try:
        time.sleep(1.2)  # simulate work
    except Exception:
        pass
    ok = _net_ok()
    with VPN_LOCK:
        VPN_STATE["state"] = "up" if ok else "error"

def _share_restart_worker():
    time.sleep(0.8)
    try:
        time.sleep(1.2)
    except Exception:
        pass
    ok = _net_ok()
    with SHARE_LOCK:
        SHARE_STATE["state"] = "up" if ok else "error"

def _tak_restart_worker():
    time.sleep(0.8)
    try:
        time.sleep(1.2)
    except Exception:
        pass
    ok = _net_ok()
    with TAK_LOCK:
        TAK_STATE["state"] = "up" if ok else "error"

def _rally_restart_worker():
    time.sleep(0.8)
    try:
        time.sleep(1.2)
    except Exception:
        pass
    ok = _net_ok()
    with RALLY_LOCK:
        RALLY_STATE["state"] = "up" if ok else "error"

def _engagebridged_restart_worker():
    time.sleep(0.8)
    try:
        time.sleep(1.2)
    except Exception:
        pass
    ok = _net_ok()
    with ENGAGEBRIDGED_LOCK:
        ENGAGEBRIDGED_STATE["state"] = "up" if ok else "error"

def _compass_restart_worker():
    time.sleep(0.8)
    try:
        time.sleep(1.2)
    except Exception:
        pass
    ok = _net_ok()
    with COMPASS_LOCK:
        COMPASS_STATE["state"] = "up" if ok else "error"

# ---- VPN endpoints ----
@app.route("/api/vpn/status")
def vpn_status():
    with VPN_LOCK:
        return jsonify(VPN_STATE)

@app.route("/api/vpn/restart", methods=["POST"])
def vpn_restart():
    with VPN_LOCK:
        VPN_STATE["state"] = "starting"
    t = threading.Thread(target=_vpn_restart_worker, daemon=True)
    t.start()
    return jsonify({"ok": True})

@app.route("/api/vpn/config")
def vpn_config():
    cfg = (
        "# Dummy VPN configuration\n"
        "client\n"
        "dev tun\n"
        "proto udp\n"
        "remote vpn.example.com 1194\n"
        "resolv-retry infinite\n"
        "nobind\n"
        "persist-key\n"
        "persist-tun\n"
        "cipher AES-256-GCM\n"
        "verb 3\n"
    )
    resp = make_response(cfg, 200)
    resp.mimetype = "text/plain"
    return resp

# ---- Share endpoints ----
@app.route("/api/share/status")
def share_status():
    with SHARE_LOCK:
        return jsonify(SHARE_STATE)

@app.route("/api/share/restart", methods=["POST"])
def share_restart():
    with SHARE_LOCK:
        SHARE_STATE["state"] = "starting"
    t = threading.Thread(target=_share_restart_worker, daemon=True)
    t.start()
    return jsonify({"ok": True})

@app.route("/api/share/config")
def share_config():
    cfg = (
        "# Dummy Share configuration\n"
        "share_root = /srv/share\n"
        "mode       = read-write\n"
        "max_clients= 32\n"
        "protocol   = smb\n"
    )
    resp = make_response(cfg, 200)
    resp.mimetype = "text/plain"
    return resp

# ---- TAK endpoints ----
@app.route("/api/tak/status")
def tak_status():
    with TAK_LOCK:
        return jsonify(TAK_STATE)

@app.route("/api/tak/restart", methods=["POST"])
def tak_restart():
    with TAK_LOCK:
        TAK_STATE["state"] = "starting"
    t = threading.Thread(target=_tak_restart_worker, daemon=True)
    t.start()
    return jsonify({"ok": True})

@app.route("/api/tak/config")
def tak_config():
    cfg = (
        "# Dummy TAK configuration\n"
        "tak_server   = 10.0.0.10\n"
        "tak_port     = 8089\n"
        "tls_enabled  = true\n"
        "protocol     = cot\n"
    )
    resp = make_response(cfg, 200)
    resp.mimetype = "text/plain"
    return resp

# ---- RallyPoint endpoints ----
@app.route("/api/rallypoint/status")
def rallypoint_status():
    with RALLY_LOCK:
        return jsonify(RALLY_STATE)

@app.route("/api/rallypoint/restart", methods=["POST"])
def rallypoint_restart():
    with RALLY_LOCK:
        RALLY_STATE["state"] = "starting"
    t = threading.Thread(target=_rally_restart_worker, daemon=True)
    t.start()
    return jsonify({"ok": True})

@app.route("/api/rallypoint/config")
def rallypoint_config():
    cfg = (
        "# Dummy RallyPoint configuration\n"
        "service_name   = RallyPoint\n"
        "endpoint       = 10.0.0.20\n"
        "port           = 9000\n"
        "tls_enabled    = true\n"
        "protocol       = custom\n"
    )
    resp = make_response(cfg, 200)
    resp.mimetype = "text/plain"
    return resp

# ---- Engagebridged endpoints ----
@app.route("/api/engagebridged/status")
def engagebridged_status():
    with ENGAGEBRIDGED_LOCK:
        return jsonify(ENGAGEBRIDGED_STATE)

@app.route("/api/engagebridged/restart", methods=["POST"])
def engagebridged_restart():
    with ENGAGEBRIDGED_LOCK:
        ENGAGEBRIDGED_STATE["state"] = "starting"
    t = threading.Thread(target=_engagebridged_restart_worker, daemon=True)
    t.start()
    return jsonify({"ok": True})

@app.route("/api/engagebridged/config")
def engagebridged_config():
    cfg = (
        "# Dummy Engagebridged configuration\n"
        "service_name   = Engagebridged\n"
        "bridge_host    = 10.0.0.30\n"
        "bridge_port    = 9443\n"
        "mode           = active\n"
        "protocol       = https\n"
    )
    resp = make_response(cfg, 200)
    resp.mimetype = "text/plain"
    return resp

# ---- Compass (Vidterra) endpoints ----
@app.route("/api/compass/status")
def compass_status():
    with COMPASS_LOCK:
        return jsonify(COMPASS_STATE)

@app.route("/api/compass/restart", methods=["POST"])
def compass_restart():
    with COMPASS_LOCK:
        COMPASS_STATE["state"] = "starting"
    t = threading.Thread(target=_compass_restart_worker, daemon=True)
    t.start()
    return jsonify({"ok": True})

@app.route("/api/compass/config")
def compass_config():
    cfg = (
        "# Dummy Compass (Vidterra) configuration\n"
        "service_name   = Compass (Vidterra)\n"
        "api_host       = compass.vidterra.local\n"
        "api_port       = 8443\n"
        "tls_enabled    = true\n"
        "protocol       = https\n"
    )
    resp = make_response(cfg, 200)
    resp.mimetype = "text/plain"
    return resp

# ---------------- Static images API for dropdown ----------------
@app.route("/api/static-images")
def api_static_images():
    """
    Return a list of image files under static/images with their URLs.
    """
    images_dir = os.path.join(app.static_folder or os.path.join(app.root_path, "static"), "images")
    exts = {".png", ".jpg", ".jpeg", ".svg", ".gif", ".ico", ".webp"}
    items = []
    if os.path.isdir(images_dir):
        for name in sorted(os.listdir(images_dir)):
            _, ext = os.path.splitext(name)
            if ext.lower() in exts:
                rel = f"images/{name}"
                items.append({
                    "name": name,
                    "path": rel,
                    "url": url_for("static", filename=rel)
                })
    return jsonify(items)

# ---------------- Routes ----------------
@app.route("/")
def index():
    return render_template("index.html", functions=get_all_functions())

@app.route("/debug/functions")
def debug_functions():
    return jsonify(get_all_functions())

@app.route("/function/<slug>")
def function_page(slug):
    func = get_function(slug)
    if not func:
        abort(404)
    if slug == "settings":
        return render_template("settings_console.html", func=func)
    if slug == "functions":
        netplan_files = ["01-netcfg.yaml", "50-cloud-init.yaml", "99-custom.yaml"]
        return render_template("functions_console.html", func=func, netplan_files=netplan_files)
    if slug == "help":
        return render_template("help_console.html", func=func)
    return render_template("function.html", func=func)

@app.route("/function/<slug>/option/<opt_slug>", methods=["GET", "POST"])
def option_page(slug, opt_slug):
    func = get_function(slug)
    if not func:
        abort(404)
    raw_opt = next((o for o in func.get("options", []) if o.get("slug") == opt_slug), None)
    if not raw_opt:
        abort(404)

    opt = _normalize_form_option(raw_opt)

    has_template = bool(opt.get("command_template"))
    has_form = bool(opt.get("form")) and bool((opt.get("form") or {}).get("fields"))

    if request.method == "GET":
        if has_template:
            return render_template("option_form.html", func=func, opt=opt, output=None, error=None, last_values={})
        output = None
        if isinstance(opt.get("commands"), dict):
            output = run_command_for_os(opt["commands"])
        return render_template("option.html", func=func, opt=opt, output=output)

    if not has_template:
        flash("This option does not accept a prompt.", "danger")
        return redirect(url_for("function_page", slug=slug))

    values = {}
    for f in (opt.get("form") or {}).get("fields", []):
        name = f.get("name")
        if not name:
            continue
        val = (request.form.get(name) or "").strip()
        if f.get("required") and not val:
            label = f.get("label") or name
            flash(f"Field '{label}' is required.", "danger")
            return render_template("option_form.html", func=func, opt=opt, output=None, error=None, last_values=request.form)
        values[name] = val

    output = run_command_template_for_os(opt.get("command_template", {}), values)
    return render_template("option_form.html", func=func, opt=opt, output=output, error=None, last_values=values)

# --------- Settings actions / uploads ----------
@app.route("/function/settings/action/<action>", methods=["POST"])
def settings_action(action):
    return ("", 204)

UPLOAD_DIR = os.path.join(app.root_path, "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.route("/function/settings/upload-mantle", methods=["POST"])
def settings_upload_mantle():
    f = request.files.get("mantle_pkg")
    if not f:
        return ("No file", 400)
    fname = secure_filename(f.filename or "mantle.bin")
    f.save(os.path.join(UPLOAD_DIR, fname))
    return redirect(url_for("function_page", slug="settings"))

# --------- Functions (power) ----------
def _spawn_detached(cmd_list):
    system = platform.system()
    try:
        if system == "Windows":
            DETACHED_PROCESS = 0x00000008
            CREATE_NEW_PROCESS_GROUP = 0x00000200
            subprocess.Popen(cmd_list, close_fds=True, creationflags=DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP)
        else:
            subprocess.Popen(cmd_list, close_fds=True, start_new_session=True)
        return True, ""
    except Exception as e:
        return False, str(e)

def _power_action(action: str):
    system = platform.system()
    is_windows = system == "Windows"
    is_macos = system == "Darwin"
    is_linux = system == "Linux"
    if action == "shutdown":
        if is_windows:
            cmd = ["shutdown", "/s", "/t", "0", "/f"]
        elif is_macos:
            cmd = ["osascript", "-e", 'tell application "System Events" to shut down'] if shutil.which("osascript") else ["shutdown", "-h", "now"]
        else:
            cmd = ["systemctl", "poweroff", "-i"] if shutil.which("systemctl") else ["shutdown", "-h", "now"]
    elif action == "reboot":
        if is_windows:
            cmd = ["shutdown", "/r", "/t", "0", "/f"]
        elif is_macos:
            cmd = ["osascript", "-e", 'tell application "System Events" to restart'] if shutil.which("osascript") else ["shutdown", "-r", "now"]
        else:
            cmd = ["systemctl", "reboot", "-i"] if shutil.which("systemctl") else ["shutdown", "-r", "now"]
    else:
        return False, f"Unsupported action: {action}"
    ok, err = _spawn_detached(cmd)
    if not ok:
        return False, f"Failed to invoke power action: {err}"
    if (is_linux or is_macos) and hasattr(os, "geteuid") and os.geteuid() != 0 and cmd[0] in ("shutdown", "systemctl"):
        return True, f"{action.capitalize()} command issued (note: may require root privileges)."
    return True, f"{action.capitalize()} command issued."

@app.route("/function/functions/action/<action>", methods=["POST"])
def functions_action(action):
    action = (action or "").strip().lower()
    if action in ("shutdown", "reboot"):
        ok, msg = _power_action(action)
        try:
            flash(msg, "info" if ok else "danger")
        except Exception:
            pass
        return redirect(url_for("function_page", slug="functions"))
    return ("", 204)

# --------- Help (ping) ----------
def ping_host(host: str, count: int = 1, timeout_sec: int = 1) -> bool:
    system = platform.system().lower()
    if system.startswith("win"):
        cmd = ["ping", "-n", str(count), "-w", str(timeout_sec * 1000), host]
    elif system == "darwin":
        cmd = ["ping", "-c", str(count), host]
    else:
        cmd = ["ping", "-c", str(count), "-W", str(timeout_sec), host]
    try:
        rc = subprocess.call(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return rc == 0
    except FileNotFoundError:
        try:
            with socket.create_connection((host, 80), timeout=timeout_sec):
                return True
        except Exception:
            return False
    except Exception:
        return False

@app.route("/function/help/check_connections", methods=["POST"])
def check_connections():
    adapter_host = "127.0.0.1"
    gateway_host = "192.168.1.1"
    adapter_ok = ping_host(adapter_host)
    gateway_ok = ping_host(gateway_host)
    service_ok = adapter_ok and gateway_ok
    return jsonify({"adapter": adapter_ok, "gateway": gateway_ok, "service": service_ok})

# --------- Errors ----------
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404

# --------- Run ----------
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=4500, debug=True)

