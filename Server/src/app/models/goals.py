# Copyright 2019 National Technology & Engineering Solutions of Sandia, LLC (NTESS). 
# Under the terms of Contract DE-NA0003525 with NTESS, the U.S. Government retains 
# certain rights in this software.

from . import db


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
    insert_id = cursor.lastrowid
    cursor.close()
    return insert_id

def db_enter_goal(linkId, numReps, numSets, ownerId, weight, duration):
    #TODO: ensure name unique 
    query=f'INSERT INTO Goals (linkId, numReps, numSets, ownerId, weight, duration) VALUES ({linkId},{num_reps},{num_sets},{ownerId},{weight},{duration},);'
    return insert_or_set_data(query)


def db_update_goal(id, duration, num_reps, num_sets, weight):
    query=f"UPDATE GOALS SET duration={duration}, numReps={num_reps}, numSets={num_sets}, weight={weight} WHERE id={id}"
    return insert_or_set_data(query)

def db_lookup_goal(id):
    query=f"SELECT id, linkId, numReps, numSets, ownerId, weight, duration from Goals where id={id};"
    return get_data(query)


def db_lookup_goal_by_owner(owner_id):
    query=f"SELECT id, linkId, numReps, numSets, ownerId, weight, duration from Goals where ownerId={owner_id};"
    return get_data(query)


def db_remove_goal(id):
    query=f'DELETE FROM Goals WHERE id={id};'
    return insert_or_set_data(query)
    