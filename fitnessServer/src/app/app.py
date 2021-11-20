# Copyright 2019 National Technology & Engineering Solutions of Sandia, LLC (NTESS). 
# Under the terms of Contract DE-NA0003525 with NTESS, the U.S. Government retains 
# certain rights in this software.

#!flask/bin/python
from flask import Flask, jsonify, make_response, request, abort
from flask_cors import CORS
from .views.users import user_bp
from .views.workouts import workouts_bp
from .views.exercises import exercises_bp
from .views.etc import test_bp, err_bp
from flask_login import LoginManager
#from config import config

# login_manager=LoginManager()

def create_app():
     # Create Flask appliaction
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
#     app.secret_key = 'super secret string' 
#     login_manager.init_app(app)
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'nsu2021'
    app.config['MYSQL_DB'] = 'fitnessDemo'
    app.config['MYSQL_HOST'] = 'localhost'
    from .models import db
    db.init_app(app)

    # REgister Bps
    app.register_blueprint(user_bp)
    app.register_blueprint(exercises_bp)
    app.register_blueprint(test_bp)
    app.register_blueprint(err_bp)
    app.register_blueprint(workouts_bp)
    print("WE ARE RUNNING")
    
    # CORS(app)
    # Load default src/config.py
    # app.config.from_object('config')
    return app
    

