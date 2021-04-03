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

def db_enter_user(username, password, firstName, lastName, email, userStatus=0):
    query=f'INSERT INTO Users(username,password,firstName, lastName, email, userStatus) VALUES({username},{password},{firstName},{lastName},{email}, {userStatus}));'
    insert_or_set_data(query)
    return

def db_lookup_user(id):
    query=f"SELECT id, username, password, email, userStatus from Users where id={id};"
    return get_data(query)

def db_lookup_user_by_name(username):
    query=f"SELECT id, username, password, email, userStatus from Users where username={username};"
    return get_data(query)

# DO WE NEED??
def db_update_user(id,username, password, firstName, lastName, email, userStatus):
    query=f'UPDATE USERS SET username={username}, password={password}, firstName={firstName}, lastName={lastName}, email={email}, userStatus={userStatus} WHERE id={id}'
    insert_or_set_data(query)

def db_remove_user(id):
    query=f'DELETE FROM Users WHERE id={id};'
    insert_or_set_data(query)
    
