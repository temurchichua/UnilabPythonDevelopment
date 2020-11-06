from flask import render_template, Blueprint
from project.models import Finds, Snakes

snakes_blueprint = Blueprint('snakes',
                              __name__,
                              template_folder='templates/snakes')

@snakes_blueprint.route('/snakelist')
def snake_list():
    snakes = Snakes.query.all()
    return render_template('snake_list.html', snakes=snakes)




@snakes_blueprint.route('/viperidae')
def viperidae():
    return render_template('viperidae.html')

@snakes_blueprint.route('/colubridae')
def colubridae():
    return render_template('colubridae.html')

@snakes_blueprint.route('/typhlopidae')
def typhlopidae():
    return render_template('typhlopidae.html')

@snakes_blueprint.route('/boidae')
def boidae():
    return render_template('boidae.html')
