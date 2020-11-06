from flask import Blueprint,render_template,redirect,url_for
from myproject import db
from myproject.models import Teacher
from myproject.teachers.forms import AddForm

teachers_blueprint = Blueprint('teachers',
                              __name__,
                              template_folder='templates/teachers')

@teachers_blueprint.route('/add', methods=['GET', 'POST'])
def add():

    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        student_id = form.student_id.data
        # Add new teacher to database
        new_teacher = Teacher(name,student_id)
        db.session.add(new_teacher)
        db.session.commit()

        return redirect(url_for('students.list'))
    return render_template('add_teacher.html',form=form)
