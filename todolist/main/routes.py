from flask import render_template, send_from_directory

from todolist.main import blueprint

@blueprint.route("/")
def index():
    return render_template("pages/index.html", current_page="home")

@blueprint.route("/about")
def about():
    return render_template("pages/about.html", current_page="about")

@blueprint.route("/contact")
def contact():
    return render_template("pages/contact.html", current_page="contact")

@blueprint.route("/favicon.ico")
def favicon():
    return send_from_directory("static", "img/favicon.png", mimetype="image/png")
