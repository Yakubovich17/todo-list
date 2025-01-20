from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from importlib import import_module

from todolist.config import Config

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    for module_name in ("tasks", "main", "auth"):
        module = import_module(f"todolist.{module_name}.routes")
        app.register_blueprint(module.blueprint)

    with app.app_context():
        db.create_all()

    @app.teardown_request
    def remove_session(exception=None):
        db.session.remove()

    return app
