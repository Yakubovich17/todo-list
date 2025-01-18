import os

from flask import redirect, url_for, request, render_template

from todolist import db
from todolist.auth import blueprint
from todolist.auth.forms import SignUpForm, SignInForm
from todolist.auth.models import User
from todolist.auth.utils import secure_password, verify_password

@blueprint.route("/signin", methods=["GET", "POST"])
def signin():
    form = SignInForm(request.form)

    if request.method == "GET":
        return render_template("pages/signin.html", form=form)

    if not form.validate_on_submit():
        msg = next(iter(next(iter(form.errors.values()))), None)
        return render_template("pages/signin.html", form=form, msg=msg)

    username = request.form["username"]
    password = request.form["password"]

    user = User.query.filter_by(username=username).first()

    if not user or not verify_password(user.password, password):
        return render_template("pages/signin.html", form=form, msg="Invalid username or password")

    return redirect(url_for("main.index"))

@blueprint.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignUpForm(request.form)

    if request.method == "GET":
        return render_template("pages/signup.html", form=form)

    if not form.validate_on_submit():
        msg = next(iter(next(iter(form.errors.values()))), None)
        return render_template("pages/signup.html", form=form, msg=msg)

    username = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]
    invite_code = request.form["invite_code"]

    if User.query.filter_by(username=username).first():
        return render_template("pages/signup.html", form=form, msg="Username already registered")

    if User.query.filter_by(email=email).first():
        return render_template("pages/signup.html", form=form, msg="Email already registered")

    if invite_code != os.environ.get("INVITE_CODE"):
        return render_template("pages/signup.html", form=form, msg="Invite code is not valid")

    db.session.add(User(username, email, secure_password(password)))
    db.session.commit()

    return redirect(url_for("main.index"))
