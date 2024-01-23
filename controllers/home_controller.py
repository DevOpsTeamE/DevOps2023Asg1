from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import session
from controllers.utilities.user import get_user, get_user_role_name

HomeController =Blueprint('Home', __name__, template_folder='../templates/Home/', url_prefix='/', static_folder='static', static_url_path='/static');

@HomeController.get('/')
def index():
	return render_template('index.html');

@HomeController.get('/login')
def login_page():
	if 'user' in session:
		role_name =session['role_name']
		if role_name =='Admin':
			return redirect('/admin/')
		elif role_name =='User':
			return redirect('/user/')

	return render_template('login.html')

@HomeController.post('/login')
def login():
	username =request.form['username']
	password =request.form['password']

	users =get_user(username, password)
	if len(users)==0:
		return render_template('login.html')
	else:
		user =users[0]
		role_name =get_user_role_name(user.role_id)
		assert role_name
		session['user'] =user.serialize()
		session['role_name'] =role_name

		if role_name =='Admin':
			return redirect('/admin/')
		elif role_name =='User':
			return redirect('/user/')
		return render_template('login.html')