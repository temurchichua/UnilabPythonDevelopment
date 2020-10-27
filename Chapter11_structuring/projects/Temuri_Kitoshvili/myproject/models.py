from myproject import db

class Questions(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    tags = db.Column(db.String)
    body = db.Column(db.Text)

    answers = db.relationship('Answers', backref="Questions", lazy='dynamic')

    def __init__(self, title, tags, body):
        self.title = title
        self.tags = tags
        self.body = body


class Answers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey(Questions.id))
    body = db.Column(db.Text)

    def __init__(self, body, question_id):
        self.body = body
        self.question_id = question_id

