from project import db

class Snakes(db.Model):
    __tablename__ = "snakes"

    id = db.Column(db.Integer, primary_key=True)
    species = db.Column(db.String)
    geo_name = db.Column(db.String)
    pic_url = db.Column(db.String)
    find = db.relationship('Finds', backref="snakes")

    def __init__(self, species, geo_name, pic_url):
        self.species = species
        self.geo_name = geo_name
        self.pic_url = pic_url

class Finds(db.Model):
    __tablename__ = "finds"
    id = db.Column(db.Integer, primary_key=True)
    species_id = db.Column(db.Integer, db.ForeignKey('snakes.id'))
    location = db.Column(db.String)
    date = db.Column(db.DATETIME)
    pic = db.Column(db.LargeBinary)

    def __init__(self, species_id, location, date, pic):
        self.species_id = species_id
        self.location = location
        self.date = date
        self.pic = pic

