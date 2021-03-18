
#!flask/bin/python
from flask import Flask, jsonify, make_response, request, abort
from .views.users import user_bp
from .views.workouts import workouts_bp
from .views.exercises import exercises_bp
from .views.etc import test_bp, err_bp



def create_app():
     # Create Flask appliaction
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(user_bp)
    app.register_blueprint(exercises_bp)
    app.register_blueprint(test_bp)
    app.register_blueprint(err_bp)
    app.register_blueprint(workouts_bp)
    print("WE ARE RUNNING", file=sys.stderr)
    
    # CORS(app)
    # Load default src/config.py
    # app.config.from_object('config')
    return app
    

