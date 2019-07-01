import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import bcrypt


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/cicapp'
db = SQLAlchemy(app)

from CicApp import Routes