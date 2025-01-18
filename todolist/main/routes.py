from flask import render_template

from todolist.main import blueprint

@blueprint.route("/")
def main():
    return render_template("pages/index.html")
