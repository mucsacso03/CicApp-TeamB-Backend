from flask import Flask, url_for, redirect
from flask_bcrypt import Bcrypt
from CicApp import app, db, request
from CicApp.Forms import RegForm
from CicApp.models import User
from wtforms import StringField, PasswordField, SubmitField, BooleanField

bcrypt = Bcrypt(app)


@app.route('/')
def home():
    return 'HomePage'


@app.route('/helloworld')
def hello():
    return 'HelloWorld'


usern = ''
hashed_pw = ''


@app.route('/register', methods=['POST'])
def reg():
    form = RegForm()
    '''form.username.data = "Jani"
    form.email.data = "janivok@jano.hu"
    form.password.data = "jani69"
    hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    user = User(username=form.username.data, email=form.email.data, password=hashed_pw)  #.data kellene
    '''
    usern = request.args.get('usern', '')
    passw = request.args.get('passw', '')
    email = request.args.get('email', '')
    hashed_pw = bcrypt.generate_password_hash(passw).decode('utf-8')
    user = User(username=usern, email=email, password=hashed_pw)  # .data kellene

    # db.session.add(user)
    # db.session.commit()

    return user.username


@app.route('/login')#, methods=['POST'])
def login():
    form = RegForm()

    usern1 = request.args.get('usern', '')
    passw1 = request.args.get('passw', '')
    if usern1 == usern:
        if bcrypt.check_password_hash(passw1, hashed_pw):
            return 'logged in'
    else:
        return 'nope'

