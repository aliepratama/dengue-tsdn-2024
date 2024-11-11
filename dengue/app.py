from flask import Flask, request
from dengue.controllers import index as idx, scan as scn, form as frm, handler as hdl

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

@app.errorhandler(404)
def page_not_found(e):
    if app.debug:
        return hdl.get_404(e)
    return hdl.get_404()
