from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from datetime import datetime
from app import db
from app.models import Sale, Product

sales_bp = Blueprint('sales', __name__)

@sales_bp.route('/')
def list_sales():
    query = Sale.query
    product_id = request.args.get('product_id')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    if product_id:
        query = query.filter(Sale.product_id == int(product_id))

    if start_date:
        try:
            start = datetime.strptime(start_date, "%Y-%m-%d")
            query = query.filter(Sale.date >= start)
        except ValueError:
            flash("Data de início inválida.", "warning")

    if end_date:
        try:
            end = datetime.strptime(end_date, "%Y-%m-%d")
            end = datetime.combine(end, datetime.max.time())
            query = query.filter(Sale.date <= end)
        except ValueError:
            flash("Data final inválida.", "warning")

    sales = query.order_by(Sale.date.desc()).all()
    products = {p.id: p.name for p in Product.query.all()}
    return render_template('sales.html', sales=sales, products=products)

@sales_bp.route('/register', methods=['GET', 'POST'])
def register_sale():
    if request.method == 'POST':
        try:
            product_id = int(request.form['product_id'])
            quantity = int(request.form['quantity'])
            product = Product.query.get_or_404(product_id)
            total_price = product.price * quantity

            sale = Sale(
                product_id=product_id,
                quantity=quantity,
                total_price=total_price,
                date=datetime.utcnow()
            )

            if product.stock < quantity:
                flash('Estoque insuficiente.', 'danger')
                return redirect(url_for('sales.register_sale'))

            product.stock -= quantity
            db.session.add(sale)
            db.session.commit()
            flash('Venda registrada com sucesso!', 'success')
            return redirect(url_for('sales.list_sales'))
        except Exception as e:
            db.session.rollback()
            flash(f'Erro ao registrar venda: {str(e)}', 'danger')
            return redirect(url_for('sales.register_sale'))

    products = Product.query.all()
    return render_template('register_sale.html', products=products)

@sales_bp.route('/checkout', methods=['POST'])
def checkout():
    cart = session.get('cart', {})
    if not cart:
        flash("Carrinho vazio.", "warning")
        return redirect(url_for('cart.view_cart'))

    summary = []
    total = 0
    for product_id, quantity in cart.items():
        product = Product.query.get(int(product_id))
        if not product or product.stock < quantity:
            flash(f"Estoque insuficiente para {product.name}", "danger")
            return redirect(url_for('cart.view_cart'))

        product.stock -= quantity
        total_price = product.price * quantity
        sale = Sale(product_id=product.id, quantity=quantity, total_price=total_price, date=datetime.utcnow())
        db.session.add(sale)
        total += total_price

        summary.append({
            'name': product.name,
            'quantity': quantity,
            'price': product.price,
            'subtotal': total_price
        })

    db.session.commit()
    session['cart'] = {}
    return render_template('receipt.html', summary=summary, total=total, now=datetime.now())
