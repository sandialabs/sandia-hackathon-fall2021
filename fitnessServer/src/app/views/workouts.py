# Copyright 2019 National Technology & Engineering Solutions of Sandia, LLC (NTESS). 
# Under the terms of Contract DE-NA0003525 with NTESS, the U.S. Government retains 
# certain rights in this software.
from ..models.workouts import *
from flask import Blueprint, jsonify, make_response, abort, request
from flask import current_app as app


workouts_bp = Blueprint('workout', __name__, url_prefix='/api/v1/workout')


def convertWorkoutToDict(workoutTuple):
    return {
        'id': workoutTuple[0],
        'nickname': workoutTuple[1],
        'ownerId': workoutTuple[2]],
    }

def convertGoalsToDict(goalsTuple):
    return {
        'id': goalsTuple[0],
        'linkId': goalsTuple[1], 
        'numReps': goalsTuple[2], 
        'numSets': goalsTuple[3], 
        'ownerId': goalsTuple[4], 
        'weight' : goalsTuple[5], 
        'duration' : goalsTuple[6]
    }


@ workouts_bp.route('/<int:workout_id>', methods=['GET', 'POST'])
def lookup_workout(workout_id):
    workout = db_lookup_workout_by_id(workout_id)
    if len(workout) == 0:
        abort(404)
    return jsonify({'workout': convertWorkoutToDict(workout[0])})


@ workouts_bp.route('/owner/<int:owner_id>', methods=['GET'])
def lookup_workout_by_owner(owner_id):
    owned_workouts = db_lookup_workout_by_owner(owner_id)
    if len(owned_workout) == 0:
        abort(404)
    formatted_return = [convertWorkoutToDict(w) for w in owned_workouts]
    return jsonify({'workout': formatted_return})


@ workouts_bp.route('/', methods=['POST'])
def add_workout():
    if not 'nickname' in request.json and not 'ownerId' in request.json:
        abort(405)
    nickname = request.json['nickname'],
    ownerId = request.json['ownerId'],
    db_enter_workouts(nickname, ownerId)
    new_workouts = db_lookup_workout_by_owner_and_name(nickname, owner_id)
    if len(new_workouts) == 0:
        abort(405)
    else:
        return jsonify({'workout': convertWorkoutToDict(new_workouts[0])}), 201


@ workouts_bp.route('/<int:workout_id>', methods=['PUT'])
def update_workout(workout_id):
    if not request.json:
        abort(400)
    if not 'nickname' in request.json:
        abort(405)
    matched_workout = db_lookup_workout_by_id(workout_id)
    if len(matched_workout) == 0:
        abort(404)

    # do we want to overwrite every time? currently we do not
    nickname = request.json.get('nickname', matched_workout[0][1])
    db_update_workout(matched_workout[0][0], nickname)
    updated_workout = db_lookup_workout_by_id(matched_workout[0][0])
    if len(updated_workout) == 0:
        abort(405)
    return jsonify({'workout': convertWorkoutToDict(updated_workout[0])}), 200


@ workouts_bp.route('/<int:workout_id>', methods = ['DELETE'])
def delete_workout(workout_id):
    is_valid = db_lookup_workout_by_id(workout_id)
    if len(is_valid) == 0:
        abort(405)
    db_remove_workouts(workout_id)
    is_removed = True if len(db_lookup_exercise(workout_id)) != 0 else False
    return jsonify({'result': True})

# LINK SECTION
@ workouts_bp.route('/link/<int:workout_id>', methods = ['GET'])
def get_goals_by_workout_id(workout_id):
    related_goals = db_get_goals_by_workout(workout_id)
    if len(related_goals) == 0:
        abort(404)
    converted_goals = [convertGoalsToDict(g) for g in related_goals]
    return jsonify({'goals': converted_goals})
