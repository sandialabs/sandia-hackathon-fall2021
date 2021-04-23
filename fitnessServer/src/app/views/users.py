# Copyright 2019 National Technology & Engineering Solutions of Sandia, LLC (NTESS). 
# Under the terms of Contract DE-NA0003525 with NTESS, the U.S. Government retains 
# certain rights in this software.

from ..models.user import *

from flask import Blueprint, jsonify, make_response, abort, request
from flask import current_app as app


user_bp = Blueprint('user', __name__, url_prefix='FIND ME IN THE YAML FILE!')


def convertUserToDict(userTuple):
    return {
        'id': userTuple[0],
        'username': userTuple[1],
        'password': userTuple[2],
        'firstName': userTuple[3],
        'lastName': userTuple[4],
        'email': userTuple[5],
        'userStatus': userTuple[6]
    }

# USER INFORMATION SECTION


@user_bp.route('WHERE AM I GOING?', methods=[WHATAMIDOINGTELLMEPLEASE])
## fill in a method to return something here or face the wrath of the front end!
## but also please have mercy on the database and remember users could pass you
## garbage and the database doesn't like garbage it's just a database
def methodName():
    return
