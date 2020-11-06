from flask import render_template, redirect, url_for, Blueprint
from myproject import db
from myproject.models import Student
from myproject.templates.forms import Registration, Login

student_blueprint = Blueprint('login_users',
                              __name__,
                              template_folder='templates')


@registration_blueprint.route('/registration', methods=['GET', 'POST'])
def registration():
    
    form = UserRegistration()
    
    if form.validate_on_submit():
        name = form.name.data
        surname = form.surname.data
        username = form.username.data
        email = form.email.data
        password = form.password.data

        new_user = (name, surname, username, email, password)
        db.session.add(new_user)
        db.session.commit()
        return redirect('welcome')
    return render_template('registration.html', form=form)


@login_blueprint.route('/login', methods=['GET', 'POST'])  
def login():
    
    form = LoginForm()
    
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        user = Login(username, password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('welcome'))
    return render_template('login.html', form=form)
        
    

