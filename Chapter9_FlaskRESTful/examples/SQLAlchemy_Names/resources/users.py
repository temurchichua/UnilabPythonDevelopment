from flask_restful import Resource, reqparse
from models.users import UserModel


class UserResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('first_name',
                        type=str,
                        required = True,
                        help = "Please input the first_name"
    )

    parser.add_argument('last_name',
                        type=str,
                        required = True,
                        help = "Please input the last_name"
    )

    def get(self, name=None):
        user = UserModel.find_by_first_name(name)
        if user:
            return user.json()
        return {'message': f'User {name} is not in the DB'}

    def post(self):
        # 1. get object from DBModel
        # 1.5 if object already in db return message
        data = UserResource.parser.parse_args()
        user = UserModel(data['first_name'], data['last_name'])
        # 2. Save object to DB
        # 3. Return Message
        return {'message': user.json()}

    def put(self):
        # if object with first_name in db UPDATE
        # if not CREATE
        # function
        return {'message': 'update'}

    def delete(self):
        # function
        return {'message': 'delete'}
