from myproject import db


class Registration(db.Model):
    __tablename__ = 'registration_users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    username = db.Column(db.String, db.ForeighKey('login_user.username'), unique=True)
    email = db.Column(db.String)
    password = db.Column(db.String, db.ForeighKey('login_user.password'))
    
    def __init__(self, name, surname, username, email, password):
        self.name = name
        self.surname = surname
        self. username = username
        self.email = email
        self.password = password


class Login(db.Model):
    __tablename__ = 'login_users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.relationship('Registration', backref='login_user', uselist=False)
    password = db.relationship('Registration', backref='login_user', uselist=False)

