# UserLogin Form

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Email, EqualTo, DataRequired
from wtforms import ValidationError
from myproject.models import User


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     EqualTo('pass_confirm',
                                                             message="შეყვანილი პაროლები არ დაემთხვა ერთმანეთს")])
    pass_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Registration')

    def validate_email(self, email):
        if User.query.filter_by(email=self.email.data).first():  # is not None
            raise ValidationError('ელფოსტა უკვე გამოყენებულია')

    def validate_username(self, username):
        if User.query.filter_by(username=self.username.data).first():  # is not None
            raise ValidationError('მომხმარებელი უკვე გამოყენებულია')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('log in')
