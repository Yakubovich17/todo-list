from flask import redirect, url_for

from todolist.auth import blueprint

@blueprint.route("/signin", methods=["GET", "POST"])
def signin():
    return redirect(url_for("main.index"))

@blueprint.route("/signup", methods=["GET", "POST"])
def signup():
    return redirect(url_for("main.index"))
