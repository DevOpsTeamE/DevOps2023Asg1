from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from controllers.utilities.user import get_user

HomeController =Blueprint('Home', __name__, template_folder='../templates/Home/', url_prefix='/', static_folder='static', static_url_path='/static');

@HomeController.get('/')
def index():
	return render_template('index.html');

@HomeController.get('/login')
def login_page():
	return render_template('login.html')

@HomeController.post('/login')
def login():
	username =request.form['username']
	password =request.form['password']


	users =get_user(username, password)
	if len(users)==0:
		return render_template('login.html')
	else:
		return redirect('/user/')