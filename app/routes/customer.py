from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import db, Customer
from sqlalchemy.exc import IntegrityError

customers_bp = Blueprint('customers', __name__)

@customers_bp.route('/')
def list_customers():
    customers = Customer.query.all()
    return render_template('customers.html', customers=customers)

@customers_bp.route('/register', methods=['GET', 'POST'])
def register_customer():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        phone = request.form['phone']
        birthdate = request.form['birthdate']

        existing = Customer.query.filter_by(email=email).first()
        if existing:
            flash("Email já cadastrado!", "error")
            return redirect(url_for('customers.register_customer'))

        new_customer = Customer(
            name=name,
            email=email,
            password=password,
            phone=phone,
            birthdate=birthdate
        )
        db.session.add(new_customer)
        db.session.commit()

        # ✅ Aqui mudamos o destino para a home
        flash("Cadastro realizado com sucesso!", "success")
        return redirect(url_for('home.home'))

    return render_template('register_customer.html')


@customers_bp.route('/update', methods=['POST'])
def update_customer():
    customer_id = request.form.get('id')
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    birthdate = request.form.get('birthdate')

    customer = Customer.query.get(customer_id)
    if customer:
        customer.name = name
        customer.email = email
        customer.phone = phone
        customer.birthdate = birthdate
        db.session.commit()

    return redirect(url_for('customers.list_customers'))


@customers_bp.route('/delete/<int:customer_id>', methods=['POST'])
def delete_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    db.session.delete(customer)
    db.session.commit()
    return redirect(url_for('customers.list_customers'))