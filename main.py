from flask import Flask, render_template
from controllers.home_controller import HomeController

def create_app():
    app =Flask(__name__)

    @app.route("/login")
    def loginPage():
        return render_template('login.html')


    app.register_blueprint(HomeController)
    return app