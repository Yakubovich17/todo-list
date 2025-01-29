from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, RadioField
from wtforms.validators import DataRequired, Length

class TaskCreateForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(max=128)])
    description = TextAreaField("Task Description", validators=[DataRequired()])
    color = RadioField("Color", choices=[
        ("#ffbc42", "Color 1"),
        ("#d81159", "Color 2"),
        ("#8f2d56", "Color 3"),
        ("#218380", "Color 4"),
        ("#73d2de", "Color 5")
    ], default="#000000")
    submit = SubmitField("Add Task")
