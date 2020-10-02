from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, DateTimeField, SelectField, TextAreaField, SubmitField, IntegerField, RadioField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = "Secret"


class GiftForm(FlaskForm):
    age = IntegerField('Enter the age', validators=[DataRequired()])
    price_range = RadioField('Price range:',
                             choices=[('budget', '-50'),
                                      ('medium', '50-100'),
                                      ('high', '100+')])
    occasion = SelectField("What's the occasion",
                           choices=[('bd', 'BirthDay'),
                                    ('ny', 'NewYear'),
                                    ('easter', 'Easter')])
    physical = BooleanField('Do you want the gift to be physical?')
    feedback = TextAreaField('Is there anything you would like to add?')
    submit = SubmitField('Advice')

@app.route('/', methods=['GET', 'POST'])
def home():
    gift_form = GiftForm()
    return render_template('home.html', form=gift_form)

@app.route('/thankyou')
def success():
    return render_template('thankyou.html')

app.run(debug=True)