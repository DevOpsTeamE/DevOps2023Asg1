from controllers.utilities.connection import create_connection
from controllers.models.user_model import User

def get_user(username, password):
    connection = create_connection()
    cur =connection.cursor()
    cur.execute('SELECT * FROM user WHERE username=%(username)s AND password=%(password)s', {'username':username, 'password' : password})
    results =cur.fetchall()
    cur.close()
    connection.close()
    users =[]
    for res in results:
        users.append(User(res))
    return users

def has_user(username):
    connection =create_connection()
    cur =connection.cursor()
    cur.execute('SELECT * FROM user WHERE username=%(username)s', {'username' :username})
    results =cur.fetchall()
    cur.close()
    connection.close()
    for res in results:
        if res[0] ==username:
            return True
    return False

def get_user_role_name(role_id):
    connection =create_connection()
    cur =connection.cursor()
    cur.execute('SELECT name FROM role WHERE id=%(role_id)s', {'role_id' : role_id})
    result =cur.fetchall()
    cur.close()
    connection.close()
    return result[0][0]

def actual_register_user(username, password, isactive):
    connection =create_connection()
    cur =connection.cursor()
    cur.execute('INSERT INTO user VALUES(%(username)s, %(password)s, 1, %(isactive)s)', {'username' : username, 'password' :password, \
        'isactive' :isactive})
    connection.commit()
    cur.close()
    connection.close()

def register_user(username, password):
    actual_register_user(username, password, 0)

def register_user_as_admin(username, password):
    actual_register_user(username, password, 1)