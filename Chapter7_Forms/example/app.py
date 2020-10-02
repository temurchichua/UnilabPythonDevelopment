from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm

from wtforms import (StringField, BooleanField,
                     DateTimeField, SelectField,
                     TextAreaField, SubmitField)

from wtforms.validators import DataRequired, length

app = Flask(__name__)

app.config['SECRET_KEY'] = "My_SecRet"

