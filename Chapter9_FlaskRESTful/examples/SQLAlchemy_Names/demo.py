from app import app
from app import db
from models.users import UserModel

db.create_all()

def create(first_name, last_name):
    user = UserModel(first_name, last_name)
    db.session.add(user)
    db.session.commit()


# create("Mat", "Ilda")

def read(first_name):
    '''ფუნქცია აბრუნებს ობიექტს მონაცემთა ბაზიდან შესაბამისი პირობით'''
    return UserModel.query.filter_by(first_name=first_name).first()

def update(user):
    user.last_name =

    db.session.add(user)
    db.session.commit()

# user = read("Mat")
# print(f'მომხმარებელი: {user.first_name} {user.last_name}')
# update(user, "Hew")
#
# user = read("Mat")
# print(f'მომხმარებელი: {user.first_name} {user.last_name}')


def delete(user):
    db.session.delete(user)
    db.session.commit()

list = ['Doe', 'Toe', 'Fu']

user = UserModel("Gooy", "Sury")

for last_name in list:
