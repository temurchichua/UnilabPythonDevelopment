from flask import render_template, redirect, request, url_for, Blueprint
from myproject import db
from myproject.models import Questions, Answers

questions_blueprint = Blueprint('questions', __name__, template_folder='templates/questions')


@questions_blueprint.route('/')
@questions_blueprint.route('/questions', methods=['GET'])
def questions():
    questions = Questions.query.all()
    answers = Answers
    return render_template('questions.html', questions=questions, answers=answers)


@questions_blueprint.route('/questions/question/<int:id>', methods=['GET','Post'])
def question(id):

    question = Questions.query.get(id)
    answers = Answers.query.filter_by(question_id=id).all()

    if request.method == 'POST':
        body = request.form.get('answerBody')

        answer = Answers(body, id)
        db.session.add(answer)
        db.session.commit()
        return render_template('question.html', question=question, answers=answers)

    return render_template('question.html', question=question, answers=answers)


@questions_blueprint.route('/askQuestion/', methods=['GET','Post'])
def askQuestion():

    if request.method == 'POST':
        title = request.form.get('title')
        tags = request.form.get('tags')
        body = request.form.get('questionBody')

        question = Questions(title, tags, body)
        db.session.add(question)
        db.session.commit()

        return redirect(url_for('questions.questions'))
    return render_template('askQuestion.html')