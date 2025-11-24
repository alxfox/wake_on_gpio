from flask import Flask, abort
import os
import subprocess
import sys

app = Flask(__name__)

SECRET = os.environ.get("SECRET_TOKEN")

@app.route("/gpio_start/<token>", methods=["POST"])
def gpio_start(token):
    if token != SECRET:
        abort(401)
    subprocess.Popen([sys.executable, "/app/scripts/gpio/start.py"]) # Use system python3
    return "OK\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
