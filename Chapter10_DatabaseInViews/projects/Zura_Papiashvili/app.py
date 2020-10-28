import os
from forms import  AddForm , DelForm
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app,db)

class Books(db.Model):

    __tablename__ = 'books'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.Text)
    author = db.Column(db.Text)
    price = db.Column(db.Float)

    def __init__(self,title,author,price):
        self.author = author
        self.title = title
        self.price = price

    def __repr__(self):
        return f" ID: {self.id};   სათაური: {self.title}; \t    ავტორი: {self.author};  \t    ფასი: {self.price} "

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add_book',methods=['GET','POST'])
def add_book():
    form = AddForm()

    if form.validate_on_submit():
        title = form.title.data
        author = form.author.data
        price = form.price.data
        new_book = Books(title, author, price)
        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for('book_list'))

    return render_template('add_book.html',form=form)


@app.route('/delete_book', methods=['GET', 'POST'])
def delete_book():
    form = DelForm()


    if form.validate_on_submit():
        id = form.id.data

        book = Books.query.get(id)
        db.session.delete(book)
        db.session.commit()

        return redirect(url_for('book_list'))
    return render_template('delete_book.html',form=form)


@app.route('/book_list')
def book_list():
    books = Books.query.all()
    return render_template('book_list.html',books=books)



if __name__ == '__main__':
    app.run(debug=True)