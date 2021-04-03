from ..models.test import users
from ..models.user import *

from flask import Blueprint, jsonify, make_response, abort, request
from flask import current_app as app


user_bp = Blueprint('user', __name__, url_prefix='/api/v1/user')


def convertUserToJSON(userTuple):
    return user = {
        'id': userTuple[0],
        'username': userTuple[1],
        'password': userTuple[2],
        'firstName': userTuple[3],
        'lastName': userTuple[4],
        'email': userTuple[5],
        'userStatus': userTuple[6]
    }

# USER INFORMATION SECTION


@user_bp.route('/<int:id>', methods=['GET'])
def lookup_user(id):
    user = [u for u in users if u['id'] == id]
    if len(user) == 0:
        abort(404)
    return jsonify({'user': user[0]})


@user_bp.route('/', methods=['POST'])
def add_user():
    if not request.json or (not 'username' in request.json and not 'password' in request.json):
        abort(405)

        username = request.json['username'],
        password = request.json['password'],
        firstName = request.json.get('firstName', None),
        lastName = request.json.get('lastName', None),
        email = request.json.get('email', None),
        # if no user status given, default to active
        userStatus = request.json.get('userStatus', 0)
    db_enter_user(username, password, firstName, lastName, email, userStatus)
    created_user = db_lookup_user_by_name(username)
    if (created_user):
        convertUserToJSON(created_user)
        return jsonify({'user': new_user}), 201
    else:
        abort(404)


@user_bp.route('/<int:user_id>', methods=['PUT'])
def update_username(user_id):
    if not request.json:
        abort(400)
    if 'userStatus' in request.json and type(request.json['userStatus']) is not int:
        abort(405)
    matched_user = db_lookup_user(user_id)

    if len(matched_user) == 0:
        abort(404)

    username = request.json.get('username', matched_user[1])
    password = request.json.get('password', matched_user[2])
    firstName = request.json.get('firstName', matched_user[3])
    lastName = request.json.get('lastName', matched_user[4])
    email = request.json.get('email', matched_user[5])
    userStatus = request.json.get('userStatus', matched_user[6])
    db_update_user(matched_user[0], username, password, firstName, lastName, email, userStatus)
    updated_user = db_lookup_user(matched_user[0])
    return jsonify({'user': convertUserToJSON(updated_user)}), 200


@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    found_user = db_lookup_user(user_id)
    if len(found_user) == 0:
        abort(404)
    db_remove_user(user_id)
    return jsonify({'result': True})


@user_bp.route('/login', methods=['GET'])
def login():
    if not request.json:
        abort(400)
    if 'username' not in request.json and 'password' not in request.json:
        abort(400)
    matched_user = db.db_lookup_user_by_name(request.json['username'])
    if not matched_user:
        abort(400)
    if matched_user[3] == request.json['password']:
        return jsonify({'result': True})
    else:
        return jsonify({'result': False})
