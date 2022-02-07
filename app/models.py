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
    like = db.relationship('Like', backref='pitch', lazy='dynamic')

    def __init__(self,title,category,pitch,owner_id):
        self.title=title
        self.category= category
        self.pitch=pitch
        self.owner_id = owner_id

# like model
class Like(db.Model):
    __tablename__ = 'likes'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    # save like to database
    def save_like(self):
        db.session.add(self)
        db.session.commit()
    
     # get all likes related to a single post
    @classmethod
    def get_likes(cls, post_id):
        likes = Like.query.filter_by(post_id=post_id).all()
        return likes
    
     # get like author details from author id
    @classmethod
    def get_like_author(cls, user_id):
        author = User.query.filter_by(id=user_id).first()
        return author

# comments table
class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

# save comment to database
    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    # get all comments related to a single post
    @classmethod
    def get_comments(cls, post_id):
        comments = Comment.query.filter_by(post_id=post_id).all()
        return comments

    # get comment author details from author id
    @classmethod
    def get_comment_author(cls, user_id):
        author = User.query.filter_by(id=user_id).first()
        return author

class Dislike(db.Model):
    __tablename__ = 'dislikes'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    # save like to database
    def save_dislike(self):
        db.session.add(self)
        db.session.commit()

    # get all likes related to a single post
    @classmethod
    def get_dislikes(cls, post_id):
        dislikes = Dislike.query.filter_by(post_id=post_id).all()
        return dislikes

     # get like author details from author id
    @classmethod
    def get_dislike_author(cls, user_id):
        author = User.query.filter_by(id=user_id).first()
        return author

