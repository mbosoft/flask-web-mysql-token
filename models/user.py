
from database.db import db


class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    custid = db.Column(db.String(20),unique=True)
    role = db.Column(db.String(20))

    def __init__(self, custid, role):
        self.custid = custid
        self.role = role

    def __repr__(self):
        return f"{self.id}"

# nullable=False, unique=True