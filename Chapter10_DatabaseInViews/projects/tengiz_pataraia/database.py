from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class UserModel(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String,unique=True)
    password = db.Column(db.String)

    def __init__(self,username,password):
        self.username = username
        self.password = password
    
    def __repr__(self):
        return f"( {self.username}, {self.password} )"

    @classmethod
    def get_user(self,username):
        return UserModel.query.filter_by(username=username).first()

class MessageModel(db.Model):
    __tablename__ = "messages"

    id = db.Column(db.Integer,primary_key=True)
    room = db.Column(db.String)
    username = db.Column(db.String)
    message = db.Column(db.String)
    time = db.Column(db.String)

    @staticmethod
    def getMessages(room):
        return MessageModel.query.filter_by(room=room).all()