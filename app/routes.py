from crypt import methods
from flask import render_template,request, redirect, url_for,flash,get_flashed_messages
from app import app
from app.models import User
from app import db
from app.forms import RegisterForm,LoginForm
from flask_login import login_user

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pitches')
def pitches():
    return render_template('pitch.html')

@app.route('/signUp',methods=['GET','POST']) 
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,email=form.email.data,password=form.password1.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('pitches'))
    if form.errors != {}:
        for error_message in form.errors.values():
            flash(f'There was an error with creating a user: {error_message}',category='danger')
    return render_template('signUp.html',form=form) 

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f'Suucess! You are logged in as {attempted_user.username}',category='success')
            return redirect(url_for('pitches'))
        else:
            flash('Username and password do not match! Please try again',category='danger')

    return render_template('login.html',form=form)

