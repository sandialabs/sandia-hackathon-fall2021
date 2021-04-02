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

def db_enter_goal(duration, linkId, num_reps, num_sets, ownerId, weight):
    #TODO: ensure name unique 
    query=f'INSERT INTO GOALS (duration, linkId, num_reps, num_sets, ownerId, weight) VALUES ({duration},{linkId},{num_reps},{num_sets},{ownerId},{weight});'
    insert_or_set_data(query)
    return

def db_lookup_goal(id):
    query=f"SELECT id, duration, linkId, num_reps, num_sets, ownerId, weight from GOALS where ownerId={id};"
    return get_data(query)

def db_remove_goal(id):
    query=f'DELETE FROM GOALS WHERE id={id};'
    insert_or_set_data(query)
    
