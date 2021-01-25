from flask import Flask
from flask_four.views import account
from flask_four.views import home
from flask_session import Session


def create_app():
    app = Flask(__name__)
    app.config.from_object('settings.Config')
    app.register_blueprint(account.ac)
    app.register_blueprint(home.home)
    Session(app)  # 将session替换成redis_session
    return app
