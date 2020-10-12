from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, DateTimeField, SelectField, TextAreaField, SubmitField, IntegerField, RadioField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = "Secret"


class my_Form(FlaskForm):
    name=StringField("გვითხარი შენი სახელი", validators=[DataRequired()])
    age = IntegerField('შეიყვანე შენი ასაკი', validators=[DataRequired()])
    gender = RadioField('მონიშნე სქესი:',
                             choices=[('მდედრობითი', 'female'),
                                      ('მამრობითი', 'male'),
                                      ('სხვა', 'other')])

    question = SelectField("5 რომ გაამრავლო5-ზე არის??",
                           choices=[('ocdaxuti', '25'),
                                    ('cares', 'who cares?'),
                                    ('ten', '10')])

    jail = BooleanField('ხართ თუ არა ნასამართლევი')
    about_you = TextAreaField('მოგვიყევით თქვენს შესახებ')
    submit = SubmitField('submit')

@app.route('/', methods=['GET', 'POST'])
def home():
    silly_form = my_Form()

    if silly_form.validate_on_submit():
        session["name"]=silly_form.name.data
        session['age'] = silly_form.age.data
        session['gender'] = silly_form.gender.data
        session['question'] = silly_form.question.data
        session['jail'] = silly_form.jail.data
        session['about_you'] = silly_form.about_you.data

        return redirect(url_for('success'))

    return render_template('home.html', form=silly_form)

@app.route('/thankyou')
def success():
    return render_template('thank_you.html')

app.run(debug=True)
