from flask import Blueprint
from flask import render_template

AdminController =Blueprint('Admin', __name__, template_folder='../templates/Admin/', url_prefix='/admin', static_folder='static', static_url_path='/static');

@AdminController.get('/')
def admin_index():
    return render_template('admin_index.html')