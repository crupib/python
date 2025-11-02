from flask import Flask, render_template, abort, send_from_directory
import os

app = Flask(__name__)

# ---- Serve favicon.ico from static folder ----
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon'
    )

# ---- Configure your tiles and their options here ----
FUNCTIONS = [
    {
        "slug": "data-tools",
        "title": "Data Tools",
        "description": "Import/export, quick transforms",
        "options": [
            {"slug": "import-csv", "label": "Import CSV"},
            {"slug": "export-json", "label": "Export JSON"},
            {"slug": "clean-duplicates", "label": "Clean Duplicates"},
        ],
    },
    {
        "slug": "dev-ops",
        "title": "Dev & Ops",
        "description": "Builds, deployments, logs",
        "options": [
            {"slug": "trigger-build", "label": "Trigger Build"},
            {"slug": "deploy-staging", "label": "Deploy to Staging"},
            {"slug": "view-logs", "label": "View Logs"},
        ],
    },
    {
        "slug": "ml-utils",
        "title": "ML Utilities",
        "description": "Models, datasets, evaluation",
        "options": [
            {"slug": "train-model", "label": "Train Model"},
            {"slug": "evaluate", "label": "Evaluate"},
            {"slug": "browse-datasets", "label": "Browse Datasets"},
        ],
    },
]

def get_function(slug: str):
    for f in FUNCTIONS:
        if f["slug"] == slug:
            return f
    return None

def get_option(func: dict, opt_slug: str):
    for o in func["options"]:
        if o["slug"] == opt_slug:
            return o
    return None

@app.route("/")
def index():
    return render_template("index.html", functions=FUNCTIONS)

@app.route("/function/<slug>")
def function_page(slug):
    func = get_function(slug)
    if not func:
        abort(404)
    return render_template("function.html", func=func)

@app.route("/function/<slug>/option/<opt_slug>")
def option_page(slug, opt_slug):
    func = get_function(slug)
    if not func:
        abort(404)
    opt = get_option(func, opt_slug)
    if not opt:
        abort(404)
    return render_template("option.html", func=func, opt=opt)

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=4500, debug=True)

