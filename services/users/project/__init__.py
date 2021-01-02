import os
import sys
import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify




#print(app.config, file=sys.stderr)

db = SQLAlchemy()

def create_app(script_info=None):
    #create an instance of the app
    app = Flask(__name__)


    # set configurations
    app_config = os.getenv('APP_SETTINGS')
    app.config.from_object(app_config)

    # set extensions
    db.init_app(app)

    # register blueprints
    from project.api.users import users_blueprint
    app.register_blueprint(users_blueprint)


    # shell context for flask cli
    app.shell_context_processor({'app': app, 'db': db})
    return app





