from flask import Flask, render_template, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import InputRequired

import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "Password"

# database
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class BookDatabase(db.Model):
    __tablename__ = "Books"
    id = db.Column(db.Integer, primary_key=True)
    StoreId = db.Column(db.Integer)
    BookName = db.Column(db.String)
    BookAuthor = db.Column(db.String)
    BookDescription = db.Column(db.String)
    BookPrice = db.Column(db.Float)

    def __init__(self, StoreId, BookName, BookAuthor, BookDescription, BookPrice):
        self.StoreId = StoreId
        self.BookName = BookName
        self.BookAuthor = BookAuthor
        self.BookDescription = BookDescription
        self.BookPrice = BookPrice


db.create_all()

# form
class BookStore(FlaskForm):
    StoreId = IntegerField("Store ID", validators=[InputRequired()])
    BookName = StringField('Book Name', validators=[InputRequired()])
    BookAuthor = StringField('Book Author', validators=[InputRequired()])
    BookDescription = StringField('Book Description', validators=[InputRequired()])
    BookPrice = FloatField("Book Price", validators=[InputRequired()])
    submit = SubmitField('Save')



@app.route('/', methods=['GET', 'POST'])
def index():
    form = BookStore()

    if form.validate_on_submit():
        StoreId = form.StoreId.data
        BookName = form.BookName.data
        BookAuthor = form.BookAuthor.data
        BookDescription = form.BookDescription.data
        BookPrice = form.BookPrice.data
        book = BookDatabase(StoreId, BookName, BookAuthor, BookDescription, BookPrice )
        db.session.add_all(book)
        db.session.commit()

        #clean form
        form.StoreId.data = ''
        form.BookName.data = ''
        form.BookAuthor.data = ''
        form.BookDescription.data = ''
        form.BookPrice.data = ''
        return redirect('index.html', form=form)

    return render_template('index.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)







