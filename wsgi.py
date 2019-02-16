from flask import Flask
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from menu.routes import gui


app = Flask(__name__)


app.register_blueprint(gui)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
