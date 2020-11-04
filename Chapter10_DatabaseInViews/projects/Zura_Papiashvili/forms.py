from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField


class AddForm(FlaskForm):
    title = StringField('წიგნის სათაური')
    author = StringField('წიგნის ავტორი')
    price = IntegerField('წიგნის ფასი')
    submit = SubmitField('წიგნის დამატება')

class DelForm(FlaskForm):
    id = IntegerField('წიგნის იდენტიფიკატორი')
    submit = SubmitField('წიგნის წაშლა')