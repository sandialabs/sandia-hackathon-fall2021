
#!flask/bin/python
from flask import Flask, jsonify, make_response, request, abort


app = Flask(__name__)

## STATIC DATA HERE UNTIL DATABASE IS ESTABLISHED
exercises = [ 
    {
        'id': 1,
        'name': 'Weights',
        'description': 'Freeweights for arm workouts',
        'impact': 'low',
        'intensity': 'high',
        'category': 'muscles'
    }, 
    {
        'id': 2,
        'name': 'Treadmill',
        'description': 'That thing that makes your lungs hurt',
        'impact': 'medium',
        'intensity': 'high',
        'category': 'cardio'
    }, 
    {
        'id': 3,
        'name': 'Yoga',
        'description': 'Slow breathing, long stretches',
        'impact': 'low',
        'intensity': 'low',
        'category': 'stretch'
    }
]

users = [
    {
        "id": 1,
        "username": "root",
        "firstName": "Admininstrator",
        "lastName": "Account",
        "email": "god@google.com",
        "password": "abc123",
        "userStatus": 0
    },
    {
        "id": 2,
        "username": "user1",
        "firstName": "",
        "lastName": "",
        "email": "",
        "password": "abc123",
        "userStatus": 0
    }
]

workouts = [
    {
        "id": 1,
        "nickname": "Thursday Abs",
        "ownerId": 2
    },
    {
        "id": 2,
        "nickname": "Monday Cardio",
        "ownerId": 2
    }
]

# DEFAULT LANDING ZONE
@app.route('/')
def hello():
    return "You've reached the server! Plesae wave at your screen!"

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'An invalid id was passed in. Please double check this field.'}), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Unable to find any item matching criteria given.'}), 404)


## EXERCISE SECTION
@app.route('/api/v1/exercises', methods=['GET'])
def get_all_exercises():
    return jsonify({'exercises':exercises})


@app.route('/api/v1/exercises/<int:id>', methods=['GET'])
def get_exercise(id):
    exercise = [e for e in exercises if e['id'] == id]
    if len(exercise) == 0:
        abort(404)
    return jsonify({'exercise':exercise[0]})


@app.route('/api/v1/exercises', methods=['POST'])
def add_exercise():
    if not request.json or not 'name' in request.json:
        abort(405)
    new_exercise = {
        'id': exercises[-1]['id']+1,
        'name': request.json['name'],
        'description': request.json.get('description',""),
        'impact': request.json.get('impact',""),
        'intensity': request.json.get('intensity',""),
        'category': request.json.get('category', "")
    }
    exercises.append(new_exercise)
    return jsonify({'exercise': new_exercise}), 201


@app.route('/api/v1/exercises/<int:id>', methods=['PUT'])
def update_exercise(id):

    # already putting id in the url path; don't need for json body?
    if not request.json:
        abort(400)
    matched_exercise = [e for e in exercises if e['id'] == id]
    
    if len(matched_exercise) == 0:
        abort(404)

    # do we want to overwrite every time? currently we do not    
    matched_exercise[0]['name'] = request.json.get('name', matched_exercise[0]['name'])
    matched_exercise[0]['description'] = request.json.get('description', matched_exercise[0]['description'])
    matched_exercise[0]['impact'] = request.json.get('impact', matched_exercise[0]['impact'])
    matched_exercise[0]['intensity'] = request.json.get('intensity', matched_exercise[0]['intensity'])
    matched_exercise[0]['category'] = request.json.get('category', matched_exercise[0]['category'])
    return jsonify({'exercise': matched_exercise[0]}), 200


@app.route('/api/v1/exercises/<int:id>', methods=['DELETE'])
def delete_exercise(id):
    found_exercise = [e for e in exercises if e['id'] == id]
    if len(found_exercise) == 0:
        abort(404)
    exercises.remove(found_exercise[0])
    return jsonify({'result': True})


## USER INFORMATION SECTION
@app.route('/api/v1/user/<int:id>', methods=['GET'])
def lookup_user(id):
    user = [u for u in users if u['id'] == id]
    if len(user) == 0:
        abort(404)
    return jsonify({'user':user[0]})


@app.route('/api/v1/user', methods=['POST'])
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


@app.route('/api/v1/user/<int:user_id>', methods=['PUT'])
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


@app.route('/api/v1/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    found_user = [u for u in users if u['id'] == user_id]
    if len(found_user) == 0:
        abort(404)
    users.remove(found_user[0])
    return jsonify({'result': True})


@app.route('/api/v1/user/login', methods=['GET'])
def login():
    if not request.json:
        abort(400)
    if 'username' not in request.json and 'password' not in request.json:
        abort(400)
    matched_user = [u for u in users if u['username'] == request.json['username'] and u['password'] == request.json['password']]
    if len(matched_user) == 0:
        abort(400)
    return jsonify({'result': True})


## WORKOUT SECTION
@app.route('/api/v1/exercises', methods=['GET'])
def get_all_exercises():
    return jsonify({'exercises':exercises})


@app.route('/api/v1/workout/<int:workout_id>', methods=['GET'])
def lookup_workout(workout_id):
    workout = [w for w in workouts if w['id'] == workout_id]
    if len(workout) == 0:
        abort(404)
    return jsonify({'workout':workout[0]})


@app.route('/api/v1/workout/owner/<int:owner_id>', methods=['GET'])
def lookup_workout(owner_id):
    owned_workout = [w for w in workouts if w['ownerId'] == owner_id]
    if len(owned_workout) == 0:
        abort(404)
    return jsonify({'workout':owned_workout})


@app.route('/api/v1/workout', methods=['POST'])
def add_workout():
    if not 'nickname' in request.json and not 'ownerId' in request.json:
        abort(405)
    new_workout = {
        'id': workouts[-1]['id']+1,
        'nickname': request.json['nickname'],
        'ownerId': request.json['ownerId'],
    }
    workouts.append(new_workout)
    return jsonify({'workout': new_workout}), 201


@app.route('/api/v1/workout/<int:workout_id>', methods=['PUT'])
def update_workout(workout_id):
    if not request.json:
        abort(400)
    if not 'nickname' in request.json:
        abort(405)
    matched_workout = [w for w in workouts if w['id'] == workout_id]
    
    if len(matched_workout) == 0:
        abort(404)

    # do we want to overwrite every time? currently we do not    
    matched_workout[0]['nickname'] = request.json.get('nickname', matched_workout[0]['nickname'])
    return jsonify({'workout': matched_workout[0]}), 200


@app.route('/api/v1/workout/<int:workout_id>', methods=['DELETE'])
def delete_workout(workout_id):
    found_workout = [w for w in workouts if w['id'] == workout_id]
    if len(found_workout) == 0:
        abort(404)
    workouts.remove(found_workout[0])
    return jsonify({'result': True})


## GOAL SECTION


## LINK SECTION
@app.route('/api/v1/link/workout/<int:workout_id>', methods=['GET'])
def get_goals_by_workout_id(workout_id):
    # given a workout id, find all related exercises and goals
    # first get the junction item
    junctions = [j for j in exercise_workout_link if j[workoutId] == workout_id]
    # then use the junctions to get the goals
    if len(junctions) == 0:
        abort(400)
    related_goals = [g for g in goals if g[linkId] == junctions[0]]
    if len(related_goals) == 0:
        abort(404)
    return jsonify({'exercises':exercises})


@app.route('/api/v1/link/exercise', methods=['GET'])
def get_all_workouts_by_exercise_id():
    return jsonify({'exercises':exercises})


if __name__ == '__main__':
    app.run(debug=True)

