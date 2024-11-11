from flask import Flask, request
from controllers import index as idx, scan as scn, form as frm

app = Flask(__name__)

@app.route('/')
def index():
    return idx.get_home()

@app.route('/scan', methods=['GET', 'POST'])
def scan():
    if request.method == 'POST':
        return scn.post_scan()
    return scn.get_scan()

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        return frm.post_form()
    return frm.get_form()
