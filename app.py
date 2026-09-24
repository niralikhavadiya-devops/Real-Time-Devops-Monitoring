from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "DevOps Monitoring App is Running!"

@app.route("/health")
def health():
    return "Healthy"

if __name__ == "__main__":
    app.run(debug=True)