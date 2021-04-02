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

def db_enter_workouts(nickname, ownerId):
    #TODO: ensure nickname unique 
    query=f'INSERT INTO WORKOUTS (nickname, ownerId) VALUES ({nickname}, {ownerId});'
    insert_or_set_data(query)
    return

def db_lookup_workout_by_id(id):
    query=f"SELECT id, nickname, ownerId from WORKOUTS where id={id};"
    return get_data(query)

def db_lookup_workout_by_owner(ownerId):
    query=f"SELECT id, nickname, ownerId from WORKOUTS where ownerId={ownerId};"
    return get_data(query)  

def db_remove_workouts(id):
    query=f'DELETE FROM WORKOUTS WHERE id={id};'
    insert_or_set_data(query)
    
