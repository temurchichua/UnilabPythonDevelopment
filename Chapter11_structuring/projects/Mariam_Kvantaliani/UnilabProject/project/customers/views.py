from flask import Blueprint, render_template, redirect, url_for
from project import db
from project.models import Customer
from project.customers.forms import AddForm

# Blueprints ობიექტის შექმნა

customers_blueprint = Blueprint('customers',
                                __name__,
                                template_folder='templates/customers')


@customers_blueprint.route('/customers', methods=['GET', 'POST'])
def customers():
    customers = Customer.query.all()
    return render_template('customer.html', customers=customers )


@customers_blueprint.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        idNumber = form.idNumber.data
        book_id = form.book_id.data
        cunstomer = Customer(name, idNumber, book_id)
        db.session.add(cunstomer)
        db.session.commit()

        return redirect(url_for('customers.customers'))
    return render_template('customer_add.html', form=form)
