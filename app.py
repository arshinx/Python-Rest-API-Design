# Library imports
from flask import Flask

# Local Imports
import models
from resources.courses import courses_api
from resources.reviews import reviews_api

DEBUG = True
HOST  = '0.0.0.0'
PORT  = 8000

app = Flask(__name__)
app.register_blueprint(courses_api)

# Routes

@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
    models.initialize()
    app.run(debug = DEBUG, host = HOST, port = PORT)
