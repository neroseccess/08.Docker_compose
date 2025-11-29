from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return "HW2 OK: multi-stage image built and running"

@app.get("/health")
def health():
    return jsonify(status="up")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
