import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' +os.path.join(basedir, 'data.sqlite')

db = SQLAlchemy(app)
Migrate(app, db)

class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    #  One_to_one relationship
    teacher = db.relationship('Teacher', backref="students", lazy='dynamic', uselist=False)
    # One to many
    book = db.relationship('Books', backref="students", lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.teacher:
            return f"Teacher of the Student {self.name} is {self.teacher}"
        else:
            return f"Student {self.name} has no teacher yet"

    def show_books(self):
        for book in self.book:
            print(book)

class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    name = db.Column(db.String)

    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    name = db.Column(db.String)

    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

