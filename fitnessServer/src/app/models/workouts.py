# Copyright 2019 National Technology & Engineering Solutions of Sandia, LLC (NTESS). 
# Under the terms of Contract DE-NA0003525 with NTESS, the U.S. Government retains 
# certain rights in this software.

from ..app import login_manager, db


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


def db_enter_workouts(nickname, ownerId):
    query = f'INSERT INTO Workouts (nickname, ownerId) VALUES ({nickname}, {ownerId});'
    insert_or_set_data(query)
    return


def db_lookup_workout_by_id(id):
    query = f"SELECT id, nickname, ownerId from Workouts where id={id};"
    return get_data(query)


def db_lookup_workout_by_name(name):
    query = f"SELECT id, nickname, ownerId from Workouts where nickname={name};"
    return get_data(query)


def db_lookup_workout_by_owner(ownerId):
    query = f"SELECT id, nickname, ownerId from Workouts where ownerId={ownerId};"
    return get_data(query)


def db_lookup_workout_by_owner_and_name(nickname, ownerId):
    query = f"SELECT id, nickname, ownerId from Workouts where ownerId={ownerId} and nickname={nickname};"
    return get_data(query)


def db_update_workout(id, nickname):
    query = f"UPDATE Workouts SET nickname={nickname} WHERE id={id};"
    insert_or_set_data(query)


def db_remove_workouts(id):
    query = f'DELETE FROM Workouts WHERE id={id};'
    insert_or_set_data(query)


def db_get_goals_by_workout(workout_id):
    query = f"SELECT g.id, g.linkId, g.numRep, g.numSets, g.ownerId, g.weight, g.duration FROM EXERCISEWORKOUTLINKS AS e INNER JOIN WORKOUTS as w on e.workoutId = w.id INNER JOIN Goals as g on g.linkId = e.id WHERE w.workoutID={workout_id};"
    return get_data(query)