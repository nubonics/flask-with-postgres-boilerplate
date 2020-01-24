from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
# This did not work for me when I pushed to heroku, so I suggest leaving the app.config.from_objects line commented out
# app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Results


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


if __name__ == '__main__':
    app.run()
