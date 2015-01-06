import os
from datetime import datetime
from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

base_dir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()

def create_app():
	app = Flask(__name__)
	app.config['SECRET_KEY'] = 'Hard to guess key'
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'development.sqlite')
	db.init_app(app)

	#blueprint registration
	from .players import players as players_blueprint
	app.register_blueprint(players_blueprint)


	return app