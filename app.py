from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>Hello DevOps! 🚀</h1>
    <p>Version: 1.1</p>
    <p>Environment: Development</p>
    """


@app.route("/health")
def health():
    return jsonify(status="healthy")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)