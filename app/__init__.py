import bcrypt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://marcos:getaways@localhost/pitch_lab'
app.config['SECRET_KEY'] = '944d51c0258f07f940b031b2'


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
from app import routes
