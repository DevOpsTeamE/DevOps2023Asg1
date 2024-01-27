import mysql.connector

def create_connection():
	connection = mysql.connector.connect(
   	 host='127.0.0.1',
    	port=3306,
   	 user='devopsuser',
    	password='password123!',
		database='devops2023asg1')
	return connection