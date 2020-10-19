import os
from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from resources.users import UserResource
from resources.home import HomeResource

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



api = Api(app)


api.add_resource(UserResource, '/users', '/users/<string:name>')
api.add_resource(HomeResource, '/', '/home')

if __name__ == "__main__":
    from db import db
    db.init_app(app)

    Migrate(app, db)
    app.run(debug=True)
