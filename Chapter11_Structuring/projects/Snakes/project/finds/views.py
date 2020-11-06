from flask import render_template, redirect, url_for, Blueprint, request
from project import db
from project.models import Finds, Snakes
from project.finds.forms import AddFind
from io import BytesIO
import base64
import struct

finds_blueprint = Blueprint('finds',
                              __name__,
                              template_folder='templates/finds')

@finds_blueprint.route('/add', methods=['GET', 'POST'])
def add_find():
    form = AddFind()
    if form.validate_on_submit():
        species_id = form.species_id.data
        location = form.location.data
        date = form.date.data
        pic = request.files['pic'].read()
        new_find = Finds(species_id, location, date, pic)
        db.session.add(new_find)
        db.session.commit()
        return redirect(url_for('finds.thanks'))
    return render_template('add_find.html', form=form)

@finds_blueprint.route('/thanks')
def thanks():
    return render_template('thanks.html')


@finds_blueprint.route('/findslist')
def finds_list():
    finds = Finds.query.all()
    # image_64_encode = base64.encodebytes(finds[4].pic)
    # pic = image_64_encode
    return render_template('finds_list.html', finds=finds)

@finds_blueprint.route('/species/<id>')
def find_id(id):
    snake = Snakes.query.filter_by(id=id)
    finds = Finds.query.filter_by(species_id=id)
    return render_template('find_id.html', finds=finds, snake=snake)