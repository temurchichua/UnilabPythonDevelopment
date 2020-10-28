from project import db


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    autor = db.Column(db.String(50))
    description = db.Column(db.String(300))

    customer = db.relationship('Customer', backref="book", uselist=False)

    def __init__(self, title, autor, description):
        self.title = title
        self.autor = autor
        self.description = description

    def __repr__(self):
        if self.customer:
            return f"მომხმარებელმა {self.customer.name} წაიღო {self.name}."
        else:
            return f"მომხმარებელ {self.customer.name} წიგნი არ წაუღია."


class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))

    name = db.Column(db.String)
    idNumber = db.Column(db.String)

    def __init__(self, name, idNumber, book_id):
        self.name = name
        self.idNumber = idNumber
        self.book_id = book_id

    def __repr__(self):
        return f"მომხმარებლის პარამეტრები: სახელი - {self.name}, პირადი ნომერი - {self.idNumber}"
