from app import db, OrdersModel

db.create_all()

order = OrdersModel.query.filter_by(order_id=1323).first()

print(order)
