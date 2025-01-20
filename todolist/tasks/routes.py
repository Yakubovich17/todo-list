from flask import render_template, request, url_for, redirect
from flask_login.utils import login_required, current_user

from todolist import db
from todolist.tasks import blueprint
from todolist.tasks.models import Task
from todolist.tasks.forms import TaskCreateForm

@blueprint.route("/profile")
@login_required
def profile():
    form = TaskCreateForm()

    tasks = current_user.tasks
    rows = [tasks[i:i + 4] for i in range(0, len(tasks), 4)]
    return render_template("pages/profile.html", rows=rows, form=form)

@blueprint.route("/tasks", methods=["POST"])
@login_required
def create_task():
    form = TaskCreateForm(request.form)

    if not form.validate_on_submit():
        return render_template("pages/profile.html", tasks=current_user.tasks, form=form)

    title = request.form["title"]
    description = request.form["description"]
    user_id = current_user.id

    print(description)

    task = Task(title, description, user_id)

    db.session.add(task)
    db.session.commit()

    return redirect(url_for("tasks.profile"))
