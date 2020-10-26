from flask import render_template, redirect, url_for, Blueprint
from myproject import db
from myproject.models import Student
from myproject.students.forms import AddForm, DelForm

student_blueprint = Blueprint('students',
                              __name__,
                              template_folder='templates/students')



@student_blueprint.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data

        new_student = Student(name)
        db.session.add(new_student)
        db.session.commit()

        return redirect(url_for('students.list'))

    return render_template('add.html', form=form)


@student_blueprint.route('/delete', methods=['GET', 'POST'])
def delete():
    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data

        student = Student.query.get(id)
        db.session.delete(student)
        db.session.commit()

        return redirect(url_for('students.list'))

    return render_template('delete.html', form=form)

@student_blueprint.route('/list')
def list():
    students = Student.query.all()
    return render_template('list.html', students=students)
