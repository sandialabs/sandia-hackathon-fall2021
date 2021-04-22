# Copyright 2019 National Technology & Engineering Solutions of Sandia, LLC (NTESS). 
# Under the terms of Contract DE-NA0003525 with NTESS, the U.S. Government retains 
# certain rights in this software.

from . import db


def get_data(query):
    cursor = db.connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    return data


def insert_or_set_data(query):
    cursor = db.connection.cursor()
    cursor.execute(query)
    db.connection.commit()
    cursor.close()


def db_enter_exercise(name, description, impact, intensity, category):
    # TODO: ensure name unique
    query = f'INSERT INTO Exercises (name, description, impact, intensity, category) VALUES (\'{name}\',\'{description}\',\'{impact}\',\'{intensity}\',\'{category}\');'
    insert_or_set_data(query)
    return


def db_lookup_exercise(id):
    query = f"SELECT id, name, description, impact, intensity, category from Exercises where id={id};"
    return get_data(query)


def db_lookup_exercise_by_name(name):
    query = f"SELECT id, name, description, impact, intensity, category from Exercises where name=\'{name}\';"
    return get_data(query)

def db_lookup_all_exercises():
    query = f"SELECT id, name, description, impact, intensity, category from Exercises;"
    return get_data(query)


def db_update_exercise(id, name, description, impact, intensity, category):
    query = f'UPDATE EXERCISES SET name={name}, description={description}, impact={impact}, intensity={intensity}, category={category} WHERE id={id}'
    insert_or_set_data(query)


def db_remove_exercise(id):
    query = f'DELETE FROM Exercises WHERE id={id};'
    insert_or_set_data(query)

def db_lookup_workouts_by_exercise(exercise_id):
    query = f'SELECT DISTINCT w.id, w.nickname, w.ownerId from ExerciseWorkoutLinks as e INNER JOIN Workouts as w on e.workoutID = w.id WHERE e.exerciseId = {exercise_id};'
    return get_data(query)