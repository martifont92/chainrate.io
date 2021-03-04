import os
from flask import Flask, Blueprint

def create_app():
	app = Flask(__name__)

	if app.config["ENV"] == "production":
		app.config.from_object("config.ProductionConfig")
	else:
	    app.config.from_object("config.DevelopmentConfig")

	    
	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)

	return app