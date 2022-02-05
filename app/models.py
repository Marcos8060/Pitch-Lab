from enum import unique
from app import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(length=30),nullable=False, unique=True)
    email = db.Column(db.String(length=50),nullable=False,unique=True)
    password = db.Column(db.String(length=60),nullable=False)

    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = password
