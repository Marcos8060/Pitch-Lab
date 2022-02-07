from enum import unique
from app import db,login_manager
from app import bcrypt
from flask_login import UserMixin
import sys
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime




@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# user table
class User(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(length=30),nullable=False, unique=True)
    email = db.Column(db.String(length=50),nullable=False,unique=True)
    password_hash = db.Column(db.String(255),nullable=False)
    pitches = db.relationship('Pitch',backref='owned_user',lazy='dynamic')
    # comment = db.relationship('Comment', backref='owned_user', lazy='dynamic')


    sys.setrecursionlimit(1500)
    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')
 

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = password

# pitch table
class Pitch(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(200))
    category = db.Column(db.String(200))
    pitch = db.Column(db.String(255))
    owner_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    # comment = db.relationship('Comment', backref='pitch', lazy='dynamic')


    def __init__(self,title,category,pitch,owner_id):
        self.title=title
        self.category= category
        self.pitch=pitch
        self.owner_id = owner_id



# class Comment(db.Model):
#     __tablename__ = 'comments'
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#     pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
#     comment = db.Column(db.Text)
#     timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

#     def __init__(self,comment):
#         self.comment=comment
     







    
   


