from flask import Flask, render_template, abort, send_from_directory, jsonify
import os, socket, subprocess, platform

app = Flask(__name__)
app.secret_key = "dev"

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon'
    )

@app.context_processor
def inject_hostname():
    return {"hostname": socket.gethostname()}

# -------------------- Tiles --------------------
FUNCTIONS = [
    {"slug": "settings",  "title": "Settings",  "description": "Configure system options and preferences", "options": []},
    {"slug": "functions", "title": "Functions", "description": "System utilities and network tools",       "options": []},
    {"slug": "help",      "title": "Help",      "description": "Diagnostics and service controls",         "options": []},
]

def get_function(slug: str):
    return next((f for f in FUNCTIONS if f["slug"] == slug), None)

@app.route("/")
def index():
    return render_template("index.html", functions=FUNCTIONS)

@app.route("/function/<slug>")
def function_page(slug):
    func = get_function(slug)
    if not func:
        abort(404)

    if slug == "functions":
        netplan_files = ["01-netcfg.yaml", "50-cloud-init.yaml", "99-custom.yaml"]
        return render_template("functions_console.html", func=func, netplan_files=netplan_files)
    if slug == "help":
        return render_template("help_console.html", func=func)

    return render_template("function.html", func=func)

# ---------- Cross-platform ping ----------
def ping_host(host: str, count: int = 1, timeout_sec: int = 1) -> bool:
    """
    Cross-platform ping:
      - Windows: ping -n 1 -w 1000 <host>  (timeout in ms)
      - macOS:   ping -c 1 <host>          (no -W; using default behavior)
      - Linux:   ping -c 1 -W 1 <host>     (timeout in sec)
    Returns True if exit code == 0.
    """
    system = platform.system().lower()
    if system.startswith("win"):
        cmd = ["ping", "-n", str(count), "-w", str(timeout_sec * 1000), host]
    elif system == "darwin":  # macOS
        # macOS ping does not support Linux -W; keep it simple.
        cmd = ["ping", "-c", str(count), host]
    else:  # Linux and others
        cmd = ["ping", "-c", str(count), "-W", str(timeout_sec), host]

    try:
        rc = subprocess.call(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return rc == 0
    except FileNotFoundError:
        # 'ping' binary not available; best-effort TCP fallback (port 80)
        try:
            with socket.create_connection((host, 80), timeout=timeout_sec):
                return True
        except Exception:
            return False
    except Exception:
        return False

@app.route("/function/help/check_connections", methods=["POST"])
def check_connections():
    """
    Ping the adapter & gateway; service is green only if both are OK.
    Adjust IPs to match your environment.
    """
    adapter_host = "127.0.0.1"   # local adapter as a sanity check
    gateway_host = "192.168.1.1"   # your gateway; change if needed

    adapter_ok = ping_host(adapter_host)
    gateway_ok = ping_host(gateway_host)
    service_ok = adapter_ok and gateway_ok

    return jsonify({"adapter": adapter_ok, "gateway": gateway_ok, "service": service_ok})

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=4500, debug=True)

