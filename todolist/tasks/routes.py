from flask import render_template
from flask_login.utils import login_required

from todolist.tasks import blueprint

@blueprint.route("/profile")
@login_required
def profile():
    return render_template("pages/profile.html")
