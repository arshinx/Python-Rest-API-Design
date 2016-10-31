from flask import Flask

DEBUG = True
HOST  = '0.0.0.0'
PORT  = 8000

app = Flask(__name__)


# Routes

@app.route('/')
def hello_world():
    return 'Hello World'
