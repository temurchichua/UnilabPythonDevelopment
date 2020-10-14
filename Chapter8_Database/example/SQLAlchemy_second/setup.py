from app import db
from models.orders import OrdersModel

order = OrdersModel.query.filter_by(order_id=1323).first()

print(order)
