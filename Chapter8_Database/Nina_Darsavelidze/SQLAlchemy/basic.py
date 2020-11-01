import os

from flask import Flask

from flask_sqlalchemy import SQLAlchemy

print(__file__)

basedir = os.path.abspath(os.path.dirname(__file__))

print(basedir)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class GalleryGiftShop(db.Model):
    __tablename__ = "Orders"

    id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String)
    artist = db.Column(db.String)
    description = db.Column(db.String)
    price = db.Column(db.Float)

    def __init__(self, product, artist, description, price):
        self.product = product
        self.artist = artist
        self.description = description
        self.price = price

    def __reps__(self):
        return f'ეს არის {self.artist}ის ნამუშევარი არის და ღირს {self.price} ლარი'


