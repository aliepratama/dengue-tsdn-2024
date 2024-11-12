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

@app.route('/sample/<int:id>', methods=['GET'])
def sample(id:int = 0):
    return scn.sample(id)


@app.route('/form', methods=['GET', 'POST'])
@app.route('/form/<int:id>', methods=['GET'])
def form(id:int = 0):
    if request.method == 'POST':
        return frm.post_form()
    return frm.get_form(id)


@app.errorhandler(404)
def page_not_found(e):
    if app.debug:
        return hdl.get_404(e)
    return hdl.get_404()
