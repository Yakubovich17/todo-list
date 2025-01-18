from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from importlib import import_module

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object("todolist.config.Config")

    db.init_app(app)

    for module_name in ("tasks", "main", "auth"):
        module = import_module(f"todolist.{module_name}.routes")
        app.register_blueprint(module.blueprint)

    with app.app_context():
        db.create_all()

    return app
