from flask import Flask, url_for, redirect
from CicApp import app,db,bcrypt
from CicApp.Forms import RegForm
from CicApp.models import User

@app.route('/')
def home():
    return 'HomePage'

@app.route('/helloworld')
def hello():
    return 'HelloWorld'


@app.route('/register', methods=['GET', 'POST'])
def reg():
    form = RegForm()
    hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    user = User(username=form.username, email=form.email.data, password=hashed_pw)
    db.session.add(user)
    db.session.commit()

    return 'In Progress'