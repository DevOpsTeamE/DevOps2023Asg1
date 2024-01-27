from flask import Blueprint
from flask import render_template
from flask import session
from flask import request
from flask import redirect

from controllers.utilities.user import has_user, register_user_as_admin

AdminController =Blueprint('Admin', __name__, template_folder='../templates/Admin/', url_prefix='/admin', static_folder='static', static_url_path='/static');

@AdminController.get('/')
def admin_index():
    return render_template('admin_index.html')

@AdminController.get('/create')
def admin_create_account():
    return render_template('admin_createAccount.html')

@AdminController.post('/create')
def admin_create_account_post():
    username =request.form['username']
    password =request.form['password']
    if not has_user(username):
        register_user_as_admin(username, password)
        return redirect('/admin')
    else:
        return render_template('admin_createAccount.html')