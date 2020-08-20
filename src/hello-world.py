import os
import psutil
from flask import Flask, jsonify

app = Flask(__name__)
import time
## Get App Uptime
START = time.time()

def elapsed():
    running = time.time() - START
    minutes, seconds = divmod(running, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)

## Say hello world
@app.route('/')
def hello_world():
    return 'Hello!'

def cal_elapsed():
    return elapsed()

# Get app health
@app.route('/healthz')
def healthz():
    return jsonify({"status": "OK", "version": "0.0.1", "memoryUsage": memoryUse() , "uptime": cal_elapsed()})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))