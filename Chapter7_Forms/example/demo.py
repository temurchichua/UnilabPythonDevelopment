from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = "Mellon"


class UsernameForm(FlaskForm):
    username = StringField('Username ')
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    username = None

    form = UsernameForm()

    if form.validate_on_submit():
        username = form.username.data
        form.username.data = ''

    return render_template('forms.html', form=form, username=username)


if __name__ == "__main__":
    app.run(debug=True)
