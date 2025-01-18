from flask_login import UserMixin

from todolist import db

class User(db.Model, UserMixin):
    __table_name__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.LargeBinary)

    def __repr__(self):
        return f"<User {self.username}>"
