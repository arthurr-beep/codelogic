import os
import sys
import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify


#create an instance of the app
app = Flask(__name__)


# set configurations
app_config = os.getenv('APP_SETTINGS')
app.config.from_object(app_config)

#print(app.config, file=sys.stderr)

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email


@app.route('/users/hello', methods=['GET'])
def hello_hi():
    return jsonify({
        'status': 'success',
        'message': 'hi you!'
    })