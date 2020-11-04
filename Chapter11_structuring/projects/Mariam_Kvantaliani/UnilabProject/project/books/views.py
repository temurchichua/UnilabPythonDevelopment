from flask import Blueprint, render_template, redirect, url_for
from project import db
from project.models import Book
from project.books.forms import AddForm, DeleteForm

# Blueprints ობიექტის შექმნა

books_blueprint = Blueprint('books',
                            __name__,
                            template_folder='templates/books')


@books_blueprint.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        title = form.title.data
        autor = form.autor.data
        description = form.description.data

        book = Book(title, autor, description)
        db.session.add(book)
        db.session.commit()

        return redirect(url_for('books.book'))

    return render_template('add.html', form=form)


@books_blueprint.route('/delete', methods=['GET', 'POST'])
def delete():

    form = DeleteForm()
    if form.validate_on_submit():
        id = form.id.data
        book = Book.query.get(id)
        db.session.delete(book)
        db.session.commit()

        return redirect(url_for('books.book'))

    return render_template('delete.html', form=form)


@books_blueprint.route('/book')
def book():
    books = Book.query.all()

    return render_template('book.html', books=books)
