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