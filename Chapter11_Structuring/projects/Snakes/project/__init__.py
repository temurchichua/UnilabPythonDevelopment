import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = 'SECRET'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

from project.finds.views import finds_blueprint
from project.snakes.views import snakes_blueprint

app.register_blueprint(finds_blueprint, url_prefix='/finds' )
app.register_blueprint(snakes_blueprint, url_prefix='/snakes')
