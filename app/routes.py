from crypt import methods
from flask import render_template,request, redirect, url_for
from app import app
from app.models import User
from app import db

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signUp',methods=['GET','POST']) 
def register():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        check_password = request.form['checkpassword']
        user_to_create = User(username,email,password)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('pitches'))
    return render_template('signUp.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/pitches')
def pitches():
    return render_template('pitch.html')