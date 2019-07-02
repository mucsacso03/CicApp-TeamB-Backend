from flask import Flask, url_for, redirect
from flask_bcrypt import Bcrypt
from CicApp import app, db, request, jsonify
from CicApp.Forms import RegForm
from CicApp.models import User
from wtforms import StringField, PasswordField, SubmitField, BooleanField

bcrypt = Bcrypt(app)


@app.route('/')
def home():
    return 'HomePage'


@app.route('/helloworld')
def hello():
    return jsonify(msg='HelloWorld'), 200

usern = ''
hashed_pw = ""

@app.route('/register', methods=['POST'])
def reg():
    form = RegForm()
    global usern
    global hashed_pw
    usern = request.args.get('usern', '')
    passw = request.args.get('passw', '')
    email = request.args.get('email', '')
    hashed_pw = bcrypt.generate_password_hash(passw).decode('utf-8')
    user = User(username=usern, email=email, password=hashed_pw)  # .data kellene

    # db.session.add(user)
    # db.session.commit()

    return jsonify(username=user.username, email=user.email, msg='Succesfully registered'), 200


@app.route('/login', methods=['POST'])
def login():
    form = RegForm()
    global usern
    global hashed_pw
    usern1 = request.args.get('usern1', '')
    passw1 = request.args.get('passw1', '')
    if usern1 == usern and bcrypt.check_password_hash(hashed_pw, passw1):
        return jsonify(msg='Logged in', username=usern1), 200
    else:
        return jsonify(msg='Log in failed'), 200


