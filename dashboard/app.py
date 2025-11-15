from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route("/metrics")
def metrics():
    with open("latest.json") as f:
        data = json.load(f)
    return jsonify(data)

@app.route("/")
def index():
    return open("index.html").read()

app.run(host="0.0.0.0", port=5000)
