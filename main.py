import os
from flask import Flask, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}','{self.email}')"

@app.route('/')
def home():
    return 'HomePage'

@app.route('/helloworld')
def hello():
    return 'HelloWorld'


@app.route('/register', methods=['GET', 'POST'])
def reg():

    return 'In Progress'


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000))
