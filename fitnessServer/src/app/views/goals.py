from ..models.goals import *
from ..models.link import *
from flask import Blueprint, jsonify, make_response, abort, request
from flask import current_app as app


goal_bp = Blueprint('goal', __name__, url_prefix='/api/v1/goal')

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


@ goal_bp.route('/<int:goal_id>', methods=['GET', 'POST'])
def lookup_goal_by_id(goal_id):
    goal = db_lookup_goal(goal_id)
    if len(goal) == 0:
        abort(404)
    return jsonify({'goal': convertGoalsToDict(goal[0])})


@ goal_bp.route('/user/<int:owner_id>', methods=['GET'])
def lookup_goals_by_owner(owner_id):
    owned_goals = db_lookup_goal_by_owner(owner_id)
    if len(owned_goals) == 0:
        abort(404)
    formatted_return = [convertGoalsToDict(g) for g in owned_goals]
    return jsonify({'goal': formatted_return})


@ goal_bp.route('/', methods=['POST'])
def add_goal():
    if not 'ownerId' in request.json or not 'exerciseId' in request.json or 'workoutId' in request.json:
        abort(405)
    # create link 
    link_id = db_enter_link(request.json['exerciseId'], request.json['workoutId'])
    # verify that the link was created and get linkId just created
    if (link_id > 0):
        linkId = request.json.get('linkId')
        ownerId = request.json.get('ownerId')
        weight = request.json.get('weight', None)
        duration = request.json.get('duration', None)
        numReps = request.json.get(['numReps'], None)
        numSets = request.json.get(['numSets'], None)
        db_enter_goal(linkId, numReps, numSets, ownerId, weight, duration)
        new_goals = db_lookup_goal_by_contents(linkId, numReps, numSets, ownerId, weight, duration)
        if len(new_goals) == 0:
            abort(405)
        else:
            return jsonify({'goal': convertGoalsToDict(new_goal[-1])}), 201
    else:
        abort(405)


@ goal_bp.route('/<int:goal_id>', methods=['PUT'])
def update_goal(goal_id):
    if not request.json:
        abort(400)
    if not 'id' in request.json:
        abort(405)
    matched_goals = db_lookup_goal(goal_id)
    if len(matched_goals) == 0:
        abort(404)

    # do we want to overwrite every time? currently we do not
    numReps = request.json.get('nickname', matched_goals[0][1])
    numSets = request.json.get('nickname', matched_goals[0][1])
    weight = request.json.get('nickname', matched_goals[0][1])
    duration = request.json.get('nickname', matched_goals[0][1])
    db_update_goal(matched_goals[0][0], duration, num_reps, num_sets, weight)
    updated_goal = db_lookup_goal_by_contents(duration, )
    if len(updated_goal) == 0:
        abort(405)
    return jsonify({'goals': updated_goal[0]}), 200


@ goal_bp.route('/<int:goal_id>', methods = ['DELETE'])
def delete_goal(goal_id):
    is_valid = db_lookup_goal(goal_id)
    if len(is_valid) == 0:
        abort(405)
    db_remove_goal(goal_id)
    goal_removed = True if len(db_lookup_goal(goal_id)) != 0 else False
    if goal_removed:
        # remove link
        db_remove_link(is_valid[0][1])
        link_removed = True if len(db_lookup_link(is_valid[0][1])) != 0 else False
        return jsonify({'result': link_removed})
    return jsonify({'result': False})
