from flask import render_template, redirect, url_for, Blueprint
from myproject import db, app
from myproject.models import User
from myproject.forms import UserRegistration, LoginForm


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    
    form = UserRegistration()
    
    if form.validate_on_submit():
        name = form.name.data
        surname = form.surname.data
        username = form.username.data
        email = form.email.data
        password = form.password.data

        new_user = User(name, surname, username, email, password)
        db.session.add(new_user)
        db.session.commit()
        return redirect('welcome')
    return render_template('registration.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    
    form = LoginForm()
    
    if form.validate_on_submit():
        username = User.query.filter_by(username=form.username.data).first()

        password = form.password.data
        if username.check_password(password) and username is not None:
            return redirect(url_for('welcome'))

    return render_template('login.html', form=form)
        

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')
