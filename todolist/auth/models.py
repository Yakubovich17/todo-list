from flask_login import UserMixin

from todolist import db, login_manager
from todolist.tasks.models import Task

class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.LargeBinary)
    tasks = db.relationship(Task, backref="user")

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f"<User {self.username}>"

@login_manager.user_loader
def user_loader(id):
    return User.query.filter_by(id=id).first()
