from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from  flask_migrate import Migrate, MigrateCommand
import os


app = Flask(__name__)


# app.config['SQLALCHEMY_DATABASE_URI']='postgresql://marcos:getaways@localhost/pitch_lab'
# SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL').replace("postgres://", "postgresql://", 1)


app.config['SECRET_KEY'] = '944d51c0258f07f940b031b2'
login_manager = LoginManager(app)

db = SQLAlchemy(app)
migrate = Migrate(app,db)
bcrypt = Bcrypt(app)
from app import routes
