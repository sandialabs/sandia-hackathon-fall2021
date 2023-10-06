# Copyright 2019 National Technology & Engineering Solutions of Sandia, LLC (NTESS). 
# Under the terms of Contract DE-NA0003525 with NTESS, the U.S. Government retains 
# certain rights in this software.


from ..models.test import category
from ..models.exercises import *

from flask import Blueprint, jsonify, make_response, abort ,request
from flask import current_app as app


exercises_bp = Blueprint('exercises', __name__, url_prefix='/api/v1/exercises')

def validateCategory(checkValue):
    if checkValue in category:
        return True
    return False

def convertExerciseToDict(exerciseTuple):
    return {
        'id': exerciseTuple[0],
        'name': exerciseTuple[1],
        'description': exerciseTuple[2],
        'impact': exerciseTuple[3],
        'intensity': exerciseTuple[4],
        'category': exerciseTuple[5]
    }


def convertWorkoutToDict(workoutTuple):
    return {
        'id': workoutTuple[0],
        'nickname': workoutTuple[1],
        'ownerId': workoutTuple[2],
    }

@exercises_bp.route('/', methods=['POST'])
def add_exercise():
    if not request.json or not 'name' in request.json or not validateCategory(request.json['category']):
        abort(405)
    name =  request.json['name']
    description = request.json.get('description',None)
    impact = request.json.get('impact',None)
    intensity = request.json.get('intensity', None)
    category = request.json['category']
    db_enter_exercise(name,description,impact,intensity,category)
    new_exercise = db_lookup_exercise_by_name(name)
    if new_exercise:
        return jsonify({'exercise': convertExerciseToDict(new_exercise)}), 201
    else:
        abort(405)


@exercises_bp.route('/<int:id>', methods=['PUT'])
def update_exercise(id):
    if not request.json or not validateCategory(request.json['category']):
        abort(400)
    matched_exercise = db_lookup_exercise(id)
    if len(matched_exercise) ==0:
        abort(404)

    # do we want to overwrite every time? currently we do not    
    name = request.json.get('name', matched_exercise[0][0])
    description = request.json.get('description', matched_exercise[0][1])
    impact = request.json.get('impact', matched_exercise[0][2])
    intensity = request.json.get('intensity', matched_exercise[0][3])
    category = request.json.get('category', matched_exercise[0][4])
    db_update_exercise(matched_exercise[0][0])
    updated_exercise = db_lookup_user(matched_exercise[0][0])
    return jsonify({'exercise': matched_exercise[0]}), 200


@exercises_bp.route('/<int:id>', methods=['DELETE'])
def delete_exercise(id):
    is_valid = db_lookup_exercise(id)
    if len(is_valid) == 0:
        abort(405)
    db_remove_exercise(id)
    is_removed = True if len(db_lookup_exercise(id)) != 0 else False
    return jsonify({'result': is_removed})

## WORKOUT SECTION
@exercises_bp.route('/', methods=['GET'])
def get_all_exercises():
    all_exercises = db_lookup_all_exercises()
    exercises = [convertExerciseToDict(e) for e in all_exercises]
    return jsonify({'exercises':exercises})

@exercises_bp.route('/category', methods=['GET'])
def get_all_exercises_by_category():
    ## return a dictionary of exercises grouped by category
    all_exercises = db_lookup_all_exercises()
    exercises = [convertExerciseToDict(e) for e in all_exercises]
    exercises_by_category_payload = {}
    for c in category:
        exercises = [e for e in exercises if e['category'] == c]
        exercises_by_category_payload[c] = sorted(exercises, key= lambda e: e['name'])
    return jsonify({'exercises_by_category': exercises_by_category_payload})

@exercises_bp.route('/link/<int:exerciseId>', methods=['GET'])
def get_all_workouts_by_exercise_id(exerciseId):
    workouts = db_lookup_workouts_by_exercise(exerciseId)
    all_workouts = [convertWorkoutToDict(w) for w in workouts]
    return jsonify({'workouts':workouts})

