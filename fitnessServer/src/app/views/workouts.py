

from ..models.test import exercises, workouts
from flask import Blueprint, jsonify, make_response, abort ,request
from flask import current_app as app


workouts_bp = Blueprint('workout', __name__, url_prefix='/api/v1/workout')



@workouts_bp.route('/<int:workout_id>', methods=['GET','POST'])
def lookup_workout(workout_id):
    workout = [w for w in workouts if w['id'] == workout_id]
    if len(workout) == 0:
        abort(404)
    return jsonify({'workout':workout[0]})


@workouts_bp.route('/owner/<int:owner_id>', methods=['GET'])
def lookup_workout_by_owner(owner_id):
    owned_workout = [w for w in workouts if w['ownerId'] == owner_id]
    if len(owned_workout) == 0:
        abort(404)
    return jsonify({'workout':owned_workout})


@workouts_bp.route('/', methods=['POST'])
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


@workouts_bp.route('/<int:workout_id>', methods=['PUT'])
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


@workouts_bp.route('/<int:workout_id>', methods=['DELETE'])
def delete_workout(workout_id):
    found_workout = [w for w in workouts if w['id'] == workout_id]
    if len(found_workout) == 0:
        abort(404)
    workouts.remove(found_workout[0])
    return jsonify({'result': True})


## GOAL SECTION


## LINK SECTION
@workouts_bp.route('/link/<int:workout_id>', methods=['GET'])
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