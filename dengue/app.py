import os, sys
from dotenv import load_dotenv
from flask import Flask, request
from dengue.controllers import index as idx, scan as scn, form as frm, handler as hdl

load_dotenv()

def init_webhooks(base_url):
    # Update inbound traffic via APIs to use the public-facing ngrok URL
    pass

def create_app():
    app = Flask(__name__)

    # Initialize our ngrok settings into Flask
    app.config.from_mapping(
        BASE_URL="http://localhost:5000",
        USE_NGROK=os.environ.get("USE_NGROK", "False") == "True" and os.environ.get("WERKZEUG_RUN_MAIN") != "true"
    )

    if app.config["USE_NGROK"] and os.environ.get("NGROK_AUTHTOKEN"):
        # pyngrok will only be installed, and should only ever be initialized, in a dev environment
        from pyngrok import ngrok

        # Get the dev server port (defaults to 5000 for Flask, can be overridden with `--port`
        # when starting the server
        port = sys.argv[sys.argv.index("--port") + 1] if "--port" in sys.argv else "5000"

        # Open a ngrok tunnel to the dev server
        public_url = ngrok.connect(port).public_url
        print(f" * ngrok tunnel \"{public_url}\" -> \"http://127.0.0.1:{port}\"")

        # Update any base URLs or webhooks to use the public ngrok URL
        app.config["BASE_URL"] = public_url
        init_webhooks(public_url)

    # ... Initialize Blueprints and the rest of our app

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
