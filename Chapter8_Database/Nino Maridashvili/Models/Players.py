from app import db


class PlayersModel(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    power = db.Column(db.String)



    def __init__(self, name, power):
        self.name = name
        self.power = power

    def __repr__(self):
        return f"Player's name: {self.name}, power: {self.power}"