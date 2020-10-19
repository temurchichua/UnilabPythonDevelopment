from flask import Flask, render_template, session, redirect, url_for,flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, DateField,TextAreaField,SelectField,FileField
from wtforms.validators import DataRequired, Email, EqualTo
# from flask_mail import Mail, Message
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename

app = Flask(__name__)

# mail = Mail(app)
app.config['SECRET_KEY'] = 'mysecretkey'
# app.config['MAIL_SERVER'] = 'smtp.gmail.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USERNAME'] = 'papiashvil@gmail.com'
# app.config['MAIL_PASSWORD'] = 'fsdqudsdyqcvxrch'
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True
# mail = Mail(app)


class LetterForm(FlaskForm):
    file = FileField()
    letter_text = TextAreaField('Your Future letter', validators=[DataRequired()],
                              render_kw={"placeholder": "Dear future me,"})
    deliver_in = RadioField('Deliver In:',
                            choices=[('One Year', 'One Year'), ('Five Years', 'Five Years'), ('Ten Years', 'Ten Years')])
    # deliver_date = DateField('Choose A Date', validators=[DataRequired()])
    privacy = SelectField('Make This Letter', choices=[('Private', 'Private'), ('Public', 'Public, But Anonymous')])
    mail_address = StringField('Your Email', validators=[Email(), DataRequired()], render_kw={"placeholder": "Email"})
    submit = SubmitField('Send')


@app.route('/', methods=['GET', 'POST'])
def home():
    form = LetterForm()
    if form.validate_on_submit():
        session['filename']= secure_filename(form.file.data.filename)
        form.file.data.save('static/uploads/' + session['filename'])
        session["letter_text"] = form.letter_text.data
        session['deliver_in'] = form.deliver_in.data
        session['privacy'] = form.privacy.data
        session['mail_address'] = form.mail_address.data
        # msg = Message('Future me', sender='papiashvil@gmail.com', recipients=['papiashvil@gmail.com', session['mail_address'] ])
        # msg.body = session["letter_text"]

        # mail.send(msg)
        flash('Your letter was sent')
        return redirect(url_for('report'))

    return render_template('home.html', form=form)


@app.route('/report',methods=['GET','POST'])
def report():

    return render_template('report.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
