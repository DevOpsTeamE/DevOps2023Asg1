from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import session
from controllers.home_controller import user_redirect

from controllers.utilities.capstone import create_capstone, \
    has_capstone, query_capstone, \
    get_capstone_by_title, update_capstone, \
    delete_capstone_title 

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

@CapstoneController.get('/')
def query_capstone_page():
    year =request.args.get('year')
    keyword =request.args.get('keyword')
   
    if year is None or keyword is None:
        return render_template('capstone_query.html')

    capstones = query_capstone(year, keyword)
    return render_template('capstone_query_result.html', capstones =capstones)


@CapstoneController.get('/modify/<title>')
def modify_capstone_page(title):
    if title is not None and type(title) is str:
        capstone =get_capstone_by_title(title)
        return render_template('capstone_modify.html', capstone=capstone, role=session['role_name'])
    return redirect('/login')

@CapstoneController.post('/modify/<title>')
def modify_capstone_request(title):
    if title is not None and type(title) is str:
        capstone =update_capstone(title, request.form['pic'], request.form['role'], request.form['nstudents'], \
            request.form['year'], request.form['title'], \
            request.form['companyname'], \
            request.form['poc'], \
            request.form['description'])
        return render_template('capstone_modify.html', capstone=capstone)

@CapstoneController.post('/delete')
def delete_capstone():
    title =request.form['title']
    delete_capstone_title(title)
    return redirect('/capstone')