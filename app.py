from flask import Flask, Response
import psutil
from prometheus_client import Gauge, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

cpu_usage = Gauge(
    "app_cpu_usage_percent",
    "Current CPU usage percentage"
)

memory_usage = Gauge(
    "app_memory_usage_percent",
    "Current memory usage percentage"
)


@app.route("/")
def home():
    return "DevOps Monitoring App is Running!"


@app.route("/health")
def health():
    return "Healthy"


@app.route("/metrics")
def metrics():
    cpu_usage.set(psutil.cpu_percent(interval=1))
    memory_usage.set(psutil.virtual_memory().percent)

    return Response(
        generate_latest(),
        mimetype=CONTENT_TYPE_LATEST
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)