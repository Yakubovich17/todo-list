from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class SignInForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=5, max=64)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    submit = SubmitField("Sign In")

class SignUpForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=5, max=64)])
    email = EmailField("Email", validators=[DataRequired(), Email(), Length(max=64)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password", message="Passwords do not match")])
    invite_code = StringField("Invite Code", validators=[DataRequired()])
    submit = SubmitField("Sign Up")
