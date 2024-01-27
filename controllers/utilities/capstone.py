from controllers.utilities.connection import create_connection
from controllers.models.capstone_model import Capstone, CapstoneQuery

def has_capstone(title):
    connection =create_connection()
    cur =connection.cursor()
    cur.execute('SELECT title FROM capstone WHERE title=%(title)s', {'title' : title})
    results =cur.fetchall()
    cur.close()
    connection.close()
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

def query_capstone(year, keyword):
    connection =create_connection()
    cur =connection.cursor()
    cur.execute("SELECT title, pic FROM capstone WHERE title LIKE %(keyword)s AND year=%(year)s", { 'keyword' :"%" +keyword +"%", 'year':year})
    results =cur.fetchall()
    cur.close()
    connection.close()
    capstones =[]
    for res in results:
        capstones.append(CapstoneQuery(res))
    return capstones

def get_capstone_by_title(title):
    connection =create_connection()
    cur =connection.cursor()
    cur.execute('SELECT * FROM capstone WHERE title=%(title)s', {'title' : title})
    results =cur.fetchall()
    cur.close()
    connection.close()
    if len(results)==0:
        return None
    return Capstone(results[0])

def update_capstone(title, pic, role, \
    nstudents, year, newtitle, \
    companyname, poc, description):
    connection =create_connection()
    cur =connection.cursor()
    cur.execute('UPDATE capstone SET pic=%(pic)s, role_id=%(role)s, nstudent=%(nstudents)s, year=%(year)s,' \
        'title=%(newtitle)s, companyname=%(companyname)s, poc=%(poc)s, ' \
        'description=%(description)s WHERE title=%(title)s', { 'title' : title, 
            'pic' :pic, \
            'role' : role, \
            'nstudents' : nstudents, \
            'year' : year, \
            'newtitle' : newtitle, \
            'companyname' : companyname, \
            'poc' : poc, \
            'description' : description  \
        })
    connection.commit()
    cur.close()
    connection.close()
    return Capstone((pic, role, nstudents, year, newtitle, companyname, poc, description, title))

def delete_capstone_title(title):
    connection =create_connection()
    cur =connection.cursor()
    cur.execute('DELETE FROM capstone WHERE title=%(title)s', {'title' : title})
    connection.commit()
    cur.close()
    connection.close()