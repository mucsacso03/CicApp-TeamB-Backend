from flask import Flask, url_for, redirect
from flask_bcrypt import Bcrypt
from CicApp import app,db
from CicApp.Forms import RegForm
from CicApp.models import User
from wtforms import StringField, PasswordField, SubmitField, BooleanField

bcrypt = Bcrypt(app)
'''
@app.route('/')
def home():
    return 'HomePage'
'''
@app.route('/helloworld')
def hello():
    return 'HelloWorld'


@app.route('/', methods=['GET', 'POST']) #/register csak gyorsabb igy tesztelni
def reg():
    form = RegForm()
    form.username.data = "Jani"
    form.email.data = "janivok@jano.hu"
    form.password.data = "jani69"
    hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    user = User(username=form.username.data, email=form.email.data, password=hashed_pw)  #.data kellene
    #db.session.add(user)
    #db.session.commit()

    return 'In Progress'