from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import session
from controllers.utilities.user import get_user, get_user_role_name, has_user, register_user

HomeController =Blueprint('Home', __name__, template_folder='../templates/Home/', url_prefix='/', static_folder='static', static_url_path='/static');

def user_redirect():
	if 'role_name' in session:
		role_name =session['role_name']
		if role_name =='Admin':
			return redirect('/admin/')
		else:
		    return redirect('/user/')

@HomeController.get('/')
def index():
	return render_template('index.html');

def set_session(user):
	role_name =get_user_role_name(user.role_id)
	assert role_name
	session['user'] =user.serialize()
	session['role_name'] =role_name
	return role_name

@HomeController.get('/login')
def login_page():
	return user_redirect()

	return render_template('login.html')

@HomeController.post('/login')
def login():
	username =request.form['username']
	password =request.form['password']

	users =get_user(username, password)
	if len(users)==0:
		return render_template('login.html')
	else:
		role_name =set_session(users[0])
		return user_redirect()

@HomeController.post('/register')
def register():
	username =request.form['username']
	password =request.form['password']

	if not has_user(username):
		user =register_user(username, password)
	return render_template('login.html')


@HomeController.get('/logout')
def logout():
	session.clear()
	return redirect('/')