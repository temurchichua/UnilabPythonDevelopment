from basic import db, OrdersModel

db.create_all()

order1 = OrdersModel(7, 2020, "მთაწმინდა", "მზიურის პარკი", 15.50)
order2 = OrdersModel(14, 1323, "მთაწმინდა", "მზიურის პარკი", 2.50)

db.session.add_all([order1, order2])

db.session.commit()

print(order1.id)
print(order2.id)
