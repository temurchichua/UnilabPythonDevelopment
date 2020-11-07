from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from myproject.models import User


class UserRegistration(FlaskForm):
    name = StringField('Name: ', validators=[DataRequired()])
    surname = StringField('Surname: ', validators=[DataRequired()])
    username = StringField('Username: ', validators=[DataRequired(), Email()])
    email = StringField('Email: ', validators=[DataRequired()])
    password = PasswordField('Password',
                             validators=[DataRequired(), EqualTo('pass_confirm', message='Passwords Must Match!')])
    pass_confirm = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register!')

    def validate_email(self, email):
        if User.query.filter_by(email=self.email.data).first():
            raise ValidationError('This email is already used by another user!')

    def validate_username(self, username):
        if User.query.filter_by(username=self.username.data).first():
            raise ValidationError('This username is already used!')


class LoginForm(FlaskForm):
    username = StringField('Username: ', validators=[DataRequired()])
    password = StringField('Password: ', validators=[DataRequired()])
    submit = SubmitField('Login')

    def validate_password(self, password):
        if not self.check_password:
            raise ValidationError('Password is incorrect!')

