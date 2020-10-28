import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# Connects our Flask App to our Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)


class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    # One to many
    book = db.relationship('Books', backref="student", lazy='dynamic')
    #  One_to_one relationship
    # A student only has one teacher, thus uselist is False.
    # Strong assumption of 1 teacher per 1 student and vice versa.
    teacher = db.relationship('Teacher', backref="student", uselist=False)

    def __init__(self, name):
        # მხოლოდ გვჭირდება ამ ბაზის მოდელისთვის უნიკალური წევრის ატრიბუტის აღწერა
        self.name = name

    def __repr__(self):
        if self.teacher:
            return f"Teacher of the Student {self.name} is {self.teacher.name}"
        else:
            return f"Student {self.name} has no teacher yet"

    def show_books(self):
        for book in self.book:
            print(book.name)


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Connect the teacher to the Student that "owns" it.
    # We use student.id because __tablename__='student'
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    name = db.Column(db.String)

    def __init__(self, name, student_id):
        self.student_id = student_id
        self.name = name


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    name = db.Column(db.String)

    def __init__(self, name, student_id):
        self.student_id = student_id
        self.name = name
