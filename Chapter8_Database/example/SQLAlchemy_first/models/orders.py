from app import db


class OrdersModel(db.Model):
    __tablename__ = "Orders"

    id = db.Column(db.Integer, primary_key=True)
    courier = db.Column(db.Integer)
    order_id = db.Column(db.Integer)
    start_loc = db.Column(db.String)
    end_loc = db.Column(db.String)
    price = db.Column(db.Float)
    comment = db.Column(db.String)

    def __init__(self, courier, order_id, start_loc, end_loc, price):
        self.courier = courier
        self.order_id = order_id
        self.start_loc = start_loc
        self.end_loc = end_loc
        self.price = price

    def __repr__(self):
        return f'შეკვეთა {self.order_id} მოაქვს კურიერის N {self.courier}'
