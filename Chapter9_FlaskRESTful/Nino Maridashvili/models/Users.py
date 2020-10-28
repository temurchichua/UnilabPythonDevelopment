from app import db



class UserModel(db.Model):

    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String)
    last_name = db.Column(db.String)

    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def read(cls, name):
        return UserModel.query.filter_by(name=name).first()


    def delete(self):
        db.session.delete(self)
        db.session.commit()




db.create_all()
user1 = UserModel("Nino", "Mariadshvili")
