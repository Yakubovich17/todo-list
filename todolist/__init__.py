from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object("todolist.config.Config")

    return app
