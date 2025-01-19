from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class TaskCreateForm(FlaskForm):
    title = StringField("Task Title", validators=[DataRequired()])
    description = StringField("Task Description", validators=[DataRequired()])
    submit = SubmitField("Submit")
