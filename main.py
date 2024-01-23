from flask import Flask, render_template
from controllers.home_controller import HomeController
from controllers.admin_controller import AdminController
from controllers.user_controller import UserController

def create_app():
    app =Flask(__name__)
    app.secret_key ='devops2023Asg1'

    app.register_blueprint(HomeController)
    app.register_blueprint(AdminController)
    app.register_blueprint(UserController)
    return app