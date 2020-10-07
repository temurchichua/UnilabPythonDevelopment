from flask import Flask, render_template,redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, BooleanField, RadioField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = "moon"



class foodform(FlaskForm):
    username = StringField('სახელი')
    type = SelectField("კვების სტატუსი:",
                       choices=[("mt", "ხორცის მჭამელი"), ("vg", "ვეგეტარიანელი"), ("v", "ვეგანი")])
    additional = TextAreaField('დაამატეთ ინგრედიენტები რომლების დამატებაც გინდათ', validators=[DataRequired()])
    onion = BooleanField("გიყვართ ხახვი?")
    price = RadioField("ფასი:",
                       choices=[("low", "-10"), ("medium", "10-20"),
                                ("high", "20 +")])
    submit = SubmitField("შეკვეთა")



@app.route('/', methods=['GET', 'POST'])
def index():
    form = foodform()
    if form.validate_on_submit():
        session['username'] = form.username.data
        session['type'] = form.type.data
        session['additional'] = form.additional.data
        session['onion'] = form.onion.data
        session['price'] = form.price.data

        return redirect(url_for('thanks'))
    return render_template("home.html", form=form)

@app.route('/thanks')
def thanks():
    return render_template("thanks.html")
if __name__=="__main__":
    app.run(debug=True)