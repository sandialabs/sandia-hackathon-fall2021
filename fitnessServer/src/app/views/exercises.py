
from ..models.test import exercises, category

from flask import Blueprint, jsonify, make_response, abort ,request
from flask import current_app as app


exercises_bp = Blueprint('exercises', __name__, url_prefix='/api/v1/exercises')

def validateCategory(checkValue):
    if checkValue in category:
        return True
    return False

@exercises_bp.route('/', methods=['POST'])
def add_exercise():
    if not request.json or not 'name' in request.json or not validateCategory(request.json['category']):
        abort(405)
    new_exercise = {
        'id': exercises[-1]['id']+1,
        'name': request.json['name'],
        'description': request.json.get('description',""),
        'impact': request.json.get('impact',""),
        'intensity': request.json.get('intensity',""),
        'category': request.json['category']
    }
    exercises.append(new_exercise)
    return jsonify({'exercise': new_exercise}), 201


@exercises_bp.route('/<int:id>', methods=['PUT'])
def update_exercise(id):

    # already putting id in the url path; don't need for json body?
    if not request.json or not validateCategory(request.json['category']):
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


@exercises_bp.route('/<int:id>', methods=['DELETE'])
def delete_exercise(id):
    found_exercise = [e for e in exercises if e['id'] == id]
    if len(found_exercise) == 0:
        abort(404)
    exercises_bp.remove(found_exercise[0])
    return jsonify({'result': True})

## WORKOUT SECTION
@exercises_bp.route('/', methods=['GET'])
def get_all_exercises():
    return jsonify({'exercises':exercises})

@exercises_bp.route('/category', methods=['GET'])
def get_all_exercises_by_category():
    ## return a dictionary of exercises grouped by category
    exercises_by_category_payload = {}
    for c in category:
        exercises = [e for e in exercises if e['category'] == c]
        exercises_by_category_payload[c] = sorted(exercises, key= lambda e: e['name'])
    return jsonify({'exercises_by_category': exercises_by_category_payload})

@exercises_bp.route('/link', methods=['GET'])
def get_all_workouts_by_exercise_id():
    return jsonify({'exercises':exercises})

