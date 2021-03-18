from ..models.test import users

from flask import Blueprint, jsonify, make_response, abort ,request
from flask import current_app as app


user_bp = Blueprint('user', __name__, url_prefix='/api/v1/user')

## USER INFORMATION SECTION
@user_bp.route('/<int:id>', methods=['GET'])
def lookup_user(id):
    user = [u for u in users if u['id'] == id]
    if len(user) == 0:
        abort(404)
    return jsonify({'user':user[0]})


@user_bp.route('/', methods=['POST'])
def add_user():
    if not request.json or (not 'username' in request.json and not 'password' in request.json):
        abort(405)
    new_user = {
        'id': users[-1]['id']+1,
        'username': request.json['username'],
        'password': request.json['password'],
        'firstName': request.json.get('firstName',""),
        'lastName': request.json.get('lastName',""),
        'email': request.json.get('email',""),
        'userStatus': request.json.get('category', 0) #if no user status given, default to active
    }
    users.append(new_user)
    return jsonify({'user': new_user}), 201


@user_bp.route('/<int:user_id>', methods=['PUT'])
def update_username(user_id):
    if not request.json:
        abort(400)
    if 'userStatus' in request.json and type(request.json['userStatus']) is not int:
        abort(405)
    matched_user = [u for u in users if u['id'] == user_id]
    
    if len(matched_user) == 0:
        abort(404)

    # do we want to overwrite every time? currently we do not    
    matched_user[0]['username'] = request.json.get('username', matched_user[0]['username'])
    matched_user[0]['password'] = request.json.get('password', matched_user[0]['password'])
    matched_user[0]['firstName'] = request.json.get('firstName', matched_user[0]['firstName'])
    matched_user[0]['lastName'] = request.json.get('lastName', matched_user[0]['lastName'])
    matched_user[0]['email'] = request.json.get('email', matched_user[0]['email'])
    matched_user[0]['userStatus'] = request.json.get('userStatus', matched_user[0]['userStatus'])
    return jsonify({'user': matched_user[0]}), 200


@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    found_user = [u for u in users if u['id'] == user_id]
    if len(found_user) == 0:
        abort(404)
    users.remove(found_user[0])
    return jsonify({'result': True})


@user_bp.route('/login', methods=['GET'])
def login():
    if not request.json:
        abort(400)
    if 'username' not in request.json and 'password' not in request.json:
        abort(400)
    matched_user = [u for u in users if u['username'] == request.json['username'] and u['password'] == request.json['password']]
    if len(matched_user) == 0:
        abort(400)
    return jsonify({'result': True})
    
