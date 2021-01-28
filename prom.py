from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics
logging.basicConfig(level=logging.INFO)
logging.info("Setting LOGLEVEL to "INFO")
app = Flask(__name__)
metrics = PrometheusMetrics(app=app, path='/metrics')
#metrics = PrometheusMetrics(app=None, path='/metrics')
metrics.info("app_info", "App Info, this can be anything you want", version="1.0.0")
app.debug = True

@app.route("/", methods=['GET'])
def index():
    return "hello world"

if __name__ == '__main__':
    metrics.init_app(app)
    app.run(host='0.0.0.0', port=80)
