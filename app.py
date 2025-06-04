from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/health")
def health():
    return Response("OK", status=200)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
