from flask import render_template
from flask_login.utils import login_required, current_user

from todolist.tasks import blueprint

@blueprint.route("/profile")
@login_required
def profile():
    return render_template("pages/profile.html", tasks=current_user.tasks)
