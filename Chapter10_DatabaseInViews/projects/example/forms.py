from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):
    name = StringField('სტუდენტის სახელი:')
    submit = SubmitField('სტუდენტის დამატება')

class DelForm(FlaskForm):
    id = IntegerField('სტუდენტის უნიკალური იდენტიფიკატორი:')
    submit = SubmitField('სტუდენტის წაშლა')
