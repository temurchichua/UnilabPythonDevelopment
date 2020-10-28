from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, TextAreaField


class AddForm(FlaskForm):
    title = StringField('წიგნის დასახელება:')
    autor = StringField('წიგნის ავტორი:')
    description = TextAreaField('მოკლე აღწერა წიგნის შესახებ:')
    submit = SubmitField('წიგნის დამატება')


class DeleteForm(FlaskForm):
    id = IntegerField('წიგნის უნიკალური იდენთიფიკატორი:')
    submit = SubmitField('წიგნის წაშლა')
