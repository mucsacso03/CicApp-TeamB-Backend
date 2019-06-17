import os
from flask import Flask

app = Flask(__name__)

@app.route('/helloworld')
def hello():
    return 'HelloWorld'
  
if __name__ == '__main__':
  app.run(host='0.0.0.0')
