import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#############################

class OrdersModel(db.Model):
    __tablename__ = "Orders"

    id = db.Column(db.Integer, primary_key=True)
    courier = db.Column(db.Integer)
    order_id = db.Column(db.Integer)
    start_loc = db.Column(db.String)
    end_loc = db.Column(db.String)
    price = db.Column(db.Float)

    def __init__(self, courier, order_id, start_loc, end_loc, price):
        self.courier = courier
        self.order_id = order_id
        self.start_loc = start_loc
        self.end_loc = end_loc
        self.price = price

    def __repr__(self):
        return f'შეკვეთა{self.order_id} მოაქვს კურიერის N {self.courier}'

