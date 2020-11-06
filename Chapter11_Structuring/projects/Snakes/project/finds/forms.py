from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, FileField
from wtforms.fields.html5 import DateField


class AddFind(FlaskForm):
    species_id = IntegerField('შეიყვანეთ სახეობის უნიკალური იდენტიფიკატორი:')
    location = StringField('შეიყვანეთ პოვნის ლოკაცია:')
    date = DateField('შეიყვანეთ პოვნის თარიღი:')
    pic = FileField('ფოტო:')
    submit = SubmitField('ატვირთვა')


class DelFind(FlaskForm):
    id = IntegerField('')
    submit = SubmitField('წაშლა')

