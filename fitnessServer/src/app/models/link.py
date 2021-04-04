from ..app import login_manager,db

def get_data(query):
    cursor=db.connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    return data

def insert_or_set_data(query):
    cursor=db.connection.cursor()
    cursor.execute(query)
    db.connection.commit()
    cursor.close()

def db_enter_link(exerciseId,workoutId):
    query=f'INSERT INTO ExerciseWorkoutLinks (exerciseId,workoutId) VALUES ({exerciseId},{workoutId});'
    insert_or_set_data(query)
    return


def db_lookup_link_by_contents(exerciseId, workoutId):
    query=f"SELECT id, exerciseId, workoutId from ExerciseWorkoutLinks where exercise={exerciseId};"
    return get_data(query)
    

def db_lookup_link_by_exercise_id(exerciseId):
    query=f"SELECT id, exerciseId, workoutId from ExerciseWorkoutLinks where exercise={exerciseId};"
    return get_data(query)


def db_lookup_link_by_workout_id(workoutId):
    query=f"SELECT id, exerciseId, workoutId from ExerciseWorkoutLinks where workoutId={workoutId};"
    return get_data(query)


def db_lookup_link(link_id):
    query=f"SELECT id, exerciseId, workoutId from ExerciseWorkoutLinks where id={link_id};"
    return get_data(query)


def db_remove_link(id):
    query=f'DELETE FROM ExerciseWorkoutLinks WHERE id={id};'
    insert_or_set_data(query)
    