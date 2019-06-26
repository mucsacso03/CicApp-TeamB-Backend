from flask import Flask, url_for, redirect
from CicApp import app


@app.route('/')
def home():
    return 'HomePage'


@app.route('/helloworld')
def hello():
    return 'HelloWorld'


@app.route('/register', methods=['GET', 'POST'])
def reg():
    return 'In Progress'
