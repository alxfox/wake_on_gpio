from flask_cors import CORS
import os
import subprocess
import sys

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://192.168.2.9"}})

SECRET = os.environ.get("SECRET_TOKEN")

@app.route("/gpio_start", methods=["POST"])
def gpio_start():
    token = request.headers.get("X-Auth-Token")
    if token != SECRET:
        abort(401)
    subprocess.Popen([sys.executable, "/app/scripts/gpio/start.py"]) # Use system python3
    return "OK\n"

@app.route("/gpio_force_stop", methods=["POST"])
def gpio_force_stop():
    token = request.headers.get("X-Auth-Token")
    if token != SECRET:
        abort(401)
    subprocess.Popen([sys.executable, "/app/scripts/gpio/force_stop.py"]) # Use system python3
    return "OK\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
