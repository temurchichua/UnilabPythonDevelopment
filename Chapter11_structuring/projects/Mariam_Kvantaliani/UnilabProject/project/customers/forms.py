from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):

    name = StringField('მომხმარებლის სახელი/გვარი:')
    idNumber = StringField('მომხმარებლის პირადი ნომერი:')
    book_id = IntegerField("წიგნის იდენტიფიკატორი: ")
    submit = SubmitField('მომხმარებლის დამატება')

