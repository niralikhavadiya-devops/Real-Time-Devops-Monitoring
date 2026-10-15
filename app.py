from flask import Flask
import psutil

app = Flask(__name__)


@app.route("/")
def home():
    return "DevOps Monitoring App is Running!"


@app.route("/health")
def health():
    return "Healthy"


@app.route("/metrics")
def metrics():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent

    return {
        "cpu_usage_percent": cpu_usage,
        "memory_usage_percent": memory_usage
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)