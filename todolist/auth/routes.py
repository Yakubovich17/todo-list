from flask import redirect, url_for, request, render_template

from todolist.auth import blueprint
from todolist.auth.forms import SignUpForm, SignInForm

@blueprint.route("/signin", methods=["GET", "POST"])
def signin():
    form = SignInForm(request.form)

    if request.method == "GET":
        return render_template("pages/signin.html", form=form)
    return redirect(url_for("main.index"))

@blueprint.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignUpForm(request.form)

    if request.method == "GET":
        return render_template("pages/signup.html", form=form)
    return redirect(url_for("main.index"))
