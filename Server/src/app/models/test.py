# Copyright 2019 National Technology & Engineering Solutions of Sandia, LLC (NTESS). 
# Under the terms of Contract DE-NA0003525 with NTESS, the U.S. Government retains 
# certain rights in this software.

## STATIC DATA HERE UNTIL DATABASE IS ESTABLISHED
category = ['strength', 'endurance', 'flexibility', 'balance']

exercises = [ 
    {
        'id': 1,
        'name': 'Weights',
        'description': 'Freeweights for arm workouts',
        'impact': 'low',
        'intensity': 'high',
        'category': 'strength'
    }, 
    {
        'id': 2,
        'name': 'Treadmill',
        'description': 'That thing that makes your lungs hurt',
        'impact': 'medium',
        'intensity': 'high',
        'category': 'endurance'
    }, 
    {
        'id': 3,
        'name': 'Yoga',
        'description': 'Slow breathing, long stretches',
        'impact': 'low',
        'intensity': 'low',
        'category': 'flexibility'
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
    }, 
    {
        "id": 3,
        "nickname": "Around the World Muscles",
        "ownerId": 1
    }
]

goals = [
    {
        "duration": -1,
        "id": 1,
        "linkId": 0,
        "num_reps": 10,
        "num_sets": 5,
        "ownerId": 2,
        "weight": 25
    },
    {
        "duration": 45,
        "id": 2,
        "linkId": 1,
        "num_reps": -1,
        "num_sets": -1,
        "ownerId": 2,
        "weight": -1
    }
 ]
