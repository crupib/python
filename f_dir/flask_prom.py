from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app=None, path='/metrics')

app.debug = True

@app.route("/", methods=['GET'])
def index():
    return "hello world"

if __name__ == '__main__':
    metrics.init_app(app)
    app.run(host='0.0.0.0', port=80)
