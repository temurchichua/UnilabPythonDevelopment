from flask import Flask, render_template, session, redirect, url_for, flash
from flask_wtf import FlaskForm

from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename

from wtforms import (StringField, BooleanField,
                     DateTimeField, SelectField,
                     TextAreaField, SubmitField)

from wtforms.validators import DataRequired, length

app = Flask(__name__)

app.config['SECRET_KEY'] = "My_SecRet"

class SimpleSubmitDemo(FlaskForm):
    submit = SubmitField('დააჭირე')

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
    form = SimpleSubmitDemo()

    if form.validate_on_submit():
        flash('თქვენ დააჭირეთ ღილაკს!')

        return redirect(url_for('index'))

    return render_template('home.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
