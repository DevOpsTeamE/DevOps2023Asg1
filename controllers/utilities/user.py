from controllers.utilities.connection import create_connection

def get_user(username, password):
    connection = create_connection()
    cur =connection.cursor()
    cur.execute('SELECT * FROM user WHERE username=%(username)s AND password=%(password)s', {'username':username, 'password' : password})
    result =cur.fetchall()
    return result