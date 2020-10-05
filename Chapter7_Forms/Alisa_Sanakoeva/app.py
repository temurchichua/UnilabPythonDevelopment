from flask import (Flask, render_template,
                   session, redirect, url_for)
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField,
                      SelectField,
                     TextAreaField, RadioField,
                     SubmitField, FileField)
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateField

app = Flask(__name__)

app.config['SECRET_KEY'] = "Yeet"

class SnakeForm(FlaskForm):
    file = FileField('გველის ფოტო ატვირთეთ აქ: ')
    location = StringField("გველის ნახვის ადგილი:")
    comment = TextAreaField("დამატებითი ინფორმაცია ადგილის დასაკონკრეტებლად:")
    date = DateField('გველის დაფიქსირების თარიღი:')
    time = RadioField("გველის დაფიქსირების დრო:", choices=[('morning', 'დილა'),
                                                           ('noon', 'შუადღე'),
                                                           ('evening', 'საღამო'),
                                                           ('night', 'ღამე'),
                                                           ('NEI', 'არ ვიცი/ზუსტად ვერ ვიტყვი')])
    size = SelectField(u'გველის სიგრძე: ', choices=[('S', '5-30 სმ'),
                                                      ('M', '30-100 სმ'),
                                                      ('L', '100-200 სმ'),
                                                      ('NEI', 'არ ვიცი/ზუსტად ვერ ვიტყვი')])
    safe = BooleanField("გველი ცოცხლად დაუბრუნდა ბუნებას")
    submit = SubmitField('ატვირთვა')


@app.route('/', methods=['GET', 'POST'])
def snakeform():
    form = SnakeForm()

    if form.validate_on_submit():
        session['file'] = form.file.data
        session['location'] = form.location.data
        session['comment'] = form.comment.data
        session['date'] = form.date.data
        session['time'] = form.time.data
        session['size'] = form.size.data
        session['safe'] = form.safe.data
        return redirect(url_for("thanks"))

    return render_template('form.html', form=form)

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')


app.run(debug=True)

