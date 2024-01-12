from flask import Flask
from controllers.main_controller import HomeController

def create_app():
    app =Flask(__name__)

    app.register_blueprint(HomeController)
    return app