from flask import Flask, request
from controllers import index as idx, scan as scn, detect as dtc

app = Flask(__name__)

@app.route('/')
def index():
    return idx.get_home()

@app.route('/scan', methods=['GET', 'POST'])
def scan():
    if request.method == 'POST':
        return scn.post_scan()
    return scn.get_scan()

@app.route('/detect', methods=['GET', 'POST'])
def detect():
    if request.method == 'POST':
        return dtc.post_detect()
    return dtc.get_detect()
