from flask import jsonify, render_template, request, url_for, redirect
from flask_login.utils import login_required, current_user

from todolist import db
from todolist.tasks import blueprint
from todolist.tasks.models import Task
from todolist.tasks.forms import TaskCreateForm

@blueprint.route("/dashboard")
@login_required
def dashboard():
    form = TaskCreateForm()

    tasks = current_user.tasks
    rows = [tasks[i:i + 4] for i in range(0, len(tasks), 4)]
    return render_template("pages/dashboard.html", rows=rows, form=form)

@blueprint.route("/tasks", methods=["POST"])
@login_required
def create_task():
    form = TaskCreateForm(request.form)

    if not form.validate_on_submit():
        return redirect(url_for("tasks.dashboard"))

    title = request.form["title"]
    description = request.form["description"]
    user_id = current_user.id

    task = Task(title, description, user_id)

    db.session.add(task)
    db.session.commit()

    return redirect(url_for("tasks.dashboard"))

@blueprint.route("/tasks/<int:task_id>", methods=["DELETE"])
@login_required
def delete_task(task_id):
    task = Task.query.get(task_id)

    if not task:
        return jsonify({"message": "Task not found"}), 404

    if task.user_id != current_user.id:
        return jsonify({"message": "Forbidden"}), 403

    db.session.delete(task)
    db.session.commit()

    return jsonify({"message": "Success"}), 200

@blueprint.route("/tasks/<int:task_id>/toggle", methods=["POST"])
@login_required
def toggle_task(task_id):
    task = Task.query.get(task_id)

    if not task:
        return jsonify({"message": "Task not found"}), 404

    if task.user_id != current_user.id:
        return jsonify({"message": "Forbidden"}), 403

    task.completed = not task.completed

    db.session.add(task)
    db.session.commit()

    return jsonify({"message": "Success"}), 200

@blueprint.route("/tasks/<int:task_id>", methods=["PUT"])
@login_required
def edit_task(task_id):
    task = Task.query.get(task_id)

    if not task:
        return jsonify({"message": "Task not found"}), 404

    if task.user_id != current_user.id:
        return jsonify({"message": "Forbidden"}), 403

    request_data = request.json

    if not request_data:
        return jsonify({"message": "Bad Request"}), 400

    new_title = request_data["title"]
    new_description = request_data["description"]

    if not new_title.strip() or not new_description.strip():
        return jsonify({"message": "Bad Request"}), 400

    task.title = new_title
    task.description = new_description

    db.session.add(task)
    db.session.commit()

    return jsonify({"message": "Success"}), 200
