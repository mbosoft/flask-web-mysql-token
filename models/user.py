
from database.db import db


class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(30),nullable=False)
    password=db.Column(db.String(255))
    role = db.Column(db.String(20), default='user')

    def __init__(self,email,password , role):
        self.email=email
        self.password=password
        self.role = role

    def __repr__(self):
        return f"{self.id}"

