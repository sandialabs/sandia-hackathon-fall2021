from flask_login import UserMixin
from ..app import login_manager,db

class User(UserMixin):
    pass

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

def db_enter_user(username, password, email, userStatus=0):
    #TODO: ensure username and email unique 
    query=f'INSERT INTO users(username,password,email) VALUES({username},{password},{email}));'
    insert_or_set_data(query)
    return

def db_lookup_user(id):
    query=f"SELECT id, username, password, email, userStatus from USERS where id={id};"
    return get_data(query)

# DO WE NEED??
def db_update_username(username,id):
    query=f'UPDATE USERS SET username={username} WHERE id={id};'
    insert_or_set_data(query)

def db_remove_user(id):
    query=f'DELETE FROM USERS WHERE id={id};'
    insert_or_set_data(query)
    
