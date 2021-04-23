# Copyright 2019 National Technology & Engineering Solutions of Sandia, LLC (NTESS). 
# Under the terms of Contract DE-NA0003525 with NTESS, the U.S. Government retains 
# certain rights in this software.

from flask_login import UserMixin
from . import db

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

<<<<<<< HEAD
## data access to the database needs to be filled in here!
=======
def db_enter_user(username, password, firstName, lastName, email, userStatus=0):
    query=f'INSERT INTO Users(username,password,firstName, lastName, email, userStatus) VALUES(\'{username}\',\'{password}\',\'{firstName}\',\'{lastName}\',\'{email}\', {userStatus}));'
    insert_or_set_data(query)
    return

def db_lookup_user(id):
    query=f"SELECT id, username, password, firstName, lastName, email, userStatus from Users where id={id};"
    return get_data(query)

def db_lookup_user_by_name(username):
    query=f"SELECT id, username, password,  firstName, lastName, email, userStatus from Users where username=\'{username}\';"
    return get_data(query)

# DO WE NEED??
def db_update_user(id,username, password, firstName, lastName, email, userStatus):
    query=f'UPDATE USERS SET username={username}, password={password}, firstName={firstName}, lastName={lastName}, email={email}, userStatus={userStatus} WHERE id={id}'
    insert_or_set_data(query)

def db_remove_user(id):
    query=f'DELETE FROM Users WHERE id={id};'
    insert_or_set_data(query)
    
>>>>>>> e9bc1b25e4ea90ce16ed510b344afd3bf46070b6
