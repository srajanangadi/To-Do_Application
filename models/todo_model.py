from database import db
from sqlalchemy.sql import func

class Todo(db.Model):
    __tablename__ = "todo"
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(300), nullable=False)
    date_created = db.Column(db.DateTime, default=func.now())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f"<Todo {self.sno} - {self.title}>"