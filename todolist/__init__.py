from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from todolist.tasks import blueprint

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object("todolist.config.Config")

    db.init_app(app)

    app.register_blueprint(blueprint)

    with app.app_context():
        db.create_all()

    return app
