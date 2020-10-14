# id, name, price

class Products():

    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def price_generator(self, quantity):
        return quantity * self.price

product = Products(1, "ნაყინი", 2.5)

print(product.name)
