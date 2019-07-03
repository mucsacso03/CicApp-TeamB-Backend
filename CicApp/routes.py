
from flask import Flask, url_for, redirect, Response, make_response
from flask_bcrypt import Bcrypt
from werkzeug.exceptions import HTTPException

from CicApp import app, db, request, jsonify
from CicApp.forms import RegForm
from CicApp.models import User
from wtforms import StringField, PasswordField, SubmitField, BooleanField

bcrypt = Bcrypt(app)


@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html> 
    <body> 
        <p>Home Page
        <br><a href="helloworld">/helloworld</a>
        <br><a href="register">/register</a>
        <br><a href="login">/login</a>
        </p>
    </body>
    </html>'''

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

@app.errorhandler(HTTPException)
def error_handler(e):
    message = str(e)
    error_code = message[0:3]
    resp = make_response(jsonify(msg=message), error_code)
    resp.headers['Error'] = error_code
    return resp
