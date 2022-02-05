from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://marcos:getaways@localhost/pitch_lab'


db = SQLAlchemy(app)

from app import routes
