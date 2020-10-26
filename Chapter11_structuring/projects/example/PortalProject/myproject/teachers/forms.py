from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):

    name = StringField('მასწავლებლის სახელი:')
    student_id = IntegerField("სტუდენტის იდენტიფიკატორი: ")
    submit = SubmitField('მასწავლებლის დამატება')
