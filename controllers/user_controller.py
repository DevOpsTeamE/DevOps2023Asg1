from flask import Blueprint
from flask import render_template
from flask import session

UserController =Blueprint("User", __name__, template_folder="../templates/User/", url_prefix="/user", static_folder='static', static_url_path='/static');

@UserController.get("/")
def user_index():
    return render_template('user_index.html', username= session['user']['username'])