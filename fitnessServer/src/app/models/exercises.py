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

def db_enter_exercise(name, description, impact, intensity, category):
    #TODO: ensure name unique 
    query=f'INSERT INTO EXERCISES (name, description, impact, intensity, category) VALUES ({name},{description},{impact},{intensity},{category},);'
    insert_or_set_data(query)
    return

def db_lookup_exercise(id):
    query=f"SELECT id, name, description, impact, intensity, category from EXERCISES where id={id};"
    return get_data(query)
    
# DO WE NEED??
# def db_update_exercise(username,id):
#     query=f'UPDATE EXERCISES SET name=?, description=?, impact=?, intensity=?, category=? WHERE id=?'
#     insert_or_set_data(query)

def db_remove_exercise(id):
    query=f'DELETE FROM EXERCISES WHERE id={id};'
    insert_or_set_data(query)
    
