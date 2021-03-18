from flask import Blueprint, jsonify, make_response, abort ,request
from flask import current_app as app
test_bp = Blueprint('test', __name__, url_prefix='/')
err_bp = Blueprint('errors', __name__)

@err_bp.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'An invalid id was passed in. Please double check this field.'}), 400)

@err_bp.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Unable to find any item matching criteria given.'}), 404)

# DEFAULT LANDING ZONE
@test_bp.route('/')
def hello():
    return "You've reached the server! Plesae wave at your screen!"

