from flask import Blueprint
from flask import render_template

HomeController =Blueprint("Home", __name__, template_folder="../templates/Home/", url_prefix="/");

@HomeController.get("/")
def index():
	return render_template("index.html");