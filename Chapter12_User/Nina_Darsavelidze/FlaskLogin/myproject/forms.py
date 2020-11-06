from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, PasswordField
from wtforms.fields.html5 import EmailField


class UserRegistration(FlaskForm):
    name = StringField('Name: ')
    surname = StringField('Surname: ')
    username = StringField('Username: ')
    email = EmailField('Email: ')
    password = PasswordField('Password: ')


class LoginForm(FlaskForm):
    username = StringField('Username: ')
    password = PasswordField('Password: ')
