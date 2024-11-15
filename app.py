from config import SECRET_KEY
from dengue.app import app

if __name__ == '__main__':
    app.secret_key = SECRET_KEY
    app.run(host='0.0.0.0', debug=True)