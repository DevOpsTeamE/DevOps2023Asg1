from controllers.utilities.connection import create_connection
from controllers.models.user_model import User

def get_user(username, password):
    connection = create_connection()
    cur =connection.cursor()
    cur.execute('SELECT * FROM user WHERE username=%(username)s AND password=%(password)s', {'username':username, 'password' : password})
    results =cur.fetchall()
    users =[]
    for res in results:
        users.append(User(res))
    return users

def get_user_role_name(role_id):
    connection =create_connection()
    cur =connection.cursor()
    cur.execute('SELECT name FROM role WHERE id=%(role_id)s', {'role_id' : role_id})
    result =cur.fetchall()
    return result[0][0]