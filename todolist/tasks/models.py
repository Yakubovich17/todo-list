from todolist import db

class Task(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=False)
    completed = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    color = db.Column(db.String(7), nullable=False)

    def __init__(self, title, description, user_id, color):
        self.title = title
        self.description = description
        self.user_id = user_id
        self.color = color

    def __repr__(self):
        return f"<Task {self.title}>"

    def __todict__(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "user_id": self.user_id
        }
