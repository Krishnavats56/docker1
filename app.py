import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Docker with Gunicorn!"

@app.route('/api')
def api():
    return jsonify(message="This is a JSON API response.")

if __name__ == "__main__":
    port = int(os.getenv("FLASK_PORT", 5000))
    app.run(host='0.0.0.0', port=port)
