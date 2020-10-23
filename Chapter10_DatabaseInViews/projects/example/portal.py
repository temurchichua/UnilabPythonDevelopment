import os
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from forms import AddForm, DelForm  # მოგვიანებით ამ ფორმებს შევქმნით და შემოვიტანთ forms.py-დან

app = Flask(__name__)
# Key for Forms
app.config['SECRET_KEY'] = 'mysecretkey'

############################################

# SQL DATABASE კონფიგურაცია

##########################################
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)


class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"სტუდენტის სახელი - {self.name}"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data

        new_student = Student(name)
        db.session.add(new_student)
        db.session.commit()

        return redirect(url_for('list_students'))

    return render_template('add.html', form=form)


@app.route('/delete', methods=['GET', 'POST'])
def del_student():
    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data

        student = Student.query.get(id)
        db.session.delete(student)
        db.session.commit()

        return redirect(url_for('list_students'))

    return render_template('delete.html', form=form)

@app.route('/list')
def list_students():
    students = Student.query.all()
    return render_template('list.html', students=students)

if __name__ == '__main__':
    app.run(debug=True)
