import os
import sys
import json
import requests
from dotenv import load_dotenv
from flask import Flask, request
from dengue.controllers import index as idx, scan as scn, form as frm, handler as hdl
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.orm import DeclarativeBase
from pyngrok import ngrok

load_dotenv()


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


def init_webhooks(base_url):
    url = "https://api.short.io/links/lnk_4QHP_vWHlRVp7TBsqmoq1HBmxy"

    payload = json.dumps({"allowDuplicates": False, 
                        "domain": "share.aliepr.my.id", 
                        "path": 'dengue-tsdn',
                        'originalURL': base_url,
                        })
    headers = {
        'accept': "application/json",
        'content-type': "application/json",
        'authorization': os.environ.get("SHORTIO_API_KEY")
        }
    response = requests.post(url, data=payload, headers=headers)
    print(response.text)


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dengue.db"

    db.init_app(app)

    Migrate(app,db)

    app.config.from_mapping(
        BASE_URL="http://localhost:5000",
        USE_NGROK=os.environ.get("USE_NGROK", "False") == "True"
    )

    if app.config["USE_NGROK"] and os.environ.get("NGROK_AUTHTOKEN"):

        port = sys.argv[sys.argv.index(
            "--port") + 1] if "--port" in sys.argv else "5000"

        public_url = ngrok.connect(port).public_url
        print(
            f" * ngrok tunnel \"{public_url}\" -> \"http://127.0.0.1:{port}\"")

        app.config["BASE_URL"] = public_url
        init_webhooks(public_url)

    return app


app = create_app()


@app.route('/')
def index():
    return idx.get_home()


@app.route('/scan', methods=['GET', 'POST'])
def scan():
    if request.method == 'POST':
        return scn.post_scan()
    return scn.get_scan()


@app.route('/sample/<int:id>', methods=['GET'])
def sample(id: int = 0):
    return scn.sample(id)


@app.route('/form')
@app.route('/form/<int:id>')
def form(id: int = 0):
    return frm.get_form(id)


@app.route('/forminput', methods=['GET', 'POST'])
def form_input():
    if request.method == 'POST':
        return frm.post_form()
    return frm.get_form(1)


@app.errorhandler(404)
def page_not_found(e):
    if app.debug:
        return hdl.get_404(e)
    return hdl.get_404()
