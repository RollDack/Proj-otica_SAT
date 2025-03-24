from flask import Blueprint, render_template, request, redirect, url_for
from app.models import db, Product

products_bp = Blueprint('products', __name__)

@products_bp.route('/')
def list_products():
    products = Product.query.all()
    return render_template('products.html', products=products)

@products_bp.route('/add', methods=['POST'])
def add_product():
    name = request.form['name']
    price = float(request.form['price'])
    stock = int(request.form['stock'])

    product = Product(name=name, price=price, stock=stock)
    db.session.add(product)
    db.session.commit()
    return redirect(url_for('products.list_products'))

@products_bp.route('/delete/<int:product_id>', methods=['POST'])
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('products.list_products'))
