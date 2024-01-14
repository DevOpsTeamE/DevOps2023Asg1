from flask import Flask
from controllers.home_controller import HomeController

def create_app():
    app =Flask(__name__)

    @app.route("/login")
    def loginPage():
        return "Login Page"


    app.register_blueprint(HomeController)
    return app