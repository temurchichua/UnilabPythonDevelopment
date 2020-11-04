

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)

# SQL DATABASE კონფიგურაცია
app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'Book.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

#############

from project.books.views import books_blueprint
from project.customers.views import customers_blueprint
# ბლუპრინტების რეგისტრირება
app.register_blueprint(books_blueprint, url_prefix="/books")
app.register_blueprint(customers_blueprint, url_prefix='/customers')
