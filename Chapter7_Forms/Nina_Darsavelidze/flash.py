from flask import Flask, render_template, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename
from wtforms import StringField, BooleanField, DateTimeField, SelectField, TextAreaField, SubmitField, IntegerField, RadioField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Secret'

class Submit(FlaskForm):
    submit = SubmitField('Click')

class UploadForm(FlaskForm):
    file = FileField()

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = UploadForm()

    if form.validate_on_submit():
        filename = secure_filename(form.file.data.filename)
        form.file.data.save('uploads/' + filename)
        return redirect(url_for('upload'))

    return render_template('upload.html', form=form)

@app.route('/', methods = ['GET', 'POST'])
def index():
    form = Submit()

    if form.validate_on_submit():
        flash('You clicked the button')

        return redirect(url_for('index'))

    return render_template('submition.html', form=form)

app.run(port=5005, debug=True)