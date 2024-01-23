from controllers.utilities.connection import create_connection
from controllers.models.capstone_model import Capstone

def has_capstone(title):
    connection =create_connection()
    cur =connection.cursor()
    cur.execute('SELECT title FROM capstone WHERE title=%(title)s', {'title' : title})
    results =cur.fetchall()
    return len(results)!=0        

def create_capstone(pic, role, nstudents, year, title, \
    companyname, poc, description):
    connection =create_connection()
    cur =connection.cursor()
    cur.execute('INSERT INTO capstone VALUES' \
        '(%(pic)s, %(role)s, %(nstudents)s, %(year)s,' \
        '%(title)s, %(companyname)s, %(poc)s, ' \
        '%(description)s)', \
        { 'pic' :pic, \
            'role' : role, \
            'nstudents' : nstudents, \
            'year' : year, \
            'title' : title, \
            'companyname' : companyname, \
            'poc' : poc, \
            'description' : description  \
        })
    connection.commit()
    cur.close()
    connection.close()