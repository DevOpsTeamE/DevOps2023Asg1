from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import session
from controllers.utilities.capstone import create_capstone, has_capstone
from controllers.home_controller import user_redirect

CapstoneController =Blueprint('Capstone', __name__, template_folder='../templates/Capstone/', url_prefix='/capstone', static_folder='static', static_url_path='/static');

@CapstoneController.get('/create')
def captone_create():
    return render_template('capstone_create.html')

@CapstoneController.post('/create')
def capstone_create_post():
    if not (has_capstone(request.form['title'])):
        create_capstone(request.form['pic'], request.form['role'], request.form['nstudents'], \
            request.form['year'], request.form['title'], \
            request.form['companyname'], \
            request.form['poc'], \
            request.form['description'])
        return user_redirect()

    return render_template('capstone_create.html')