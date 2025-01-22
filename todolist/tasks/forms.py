from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class TaskCreateForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    description = TextAreaField("Task Description", validators=[DataRequired()])
    submit = SubmitField("Add Task")
