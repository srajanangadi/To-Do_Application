from database import db

class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), nullable = False, unique=True)
    password = db.Column(db.String(100), nullable = False)

    todos=db.relationship('Todo',backref='user',lazy=True)

    def repr(self):
        return f"<Username: {self.username}>"