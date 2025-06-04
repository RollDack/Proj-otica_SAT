from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import db, Product, InventoryLog
from datetime import datetime

stock_bp = Blueprint('stock', __name__)

@stock_bp.route('/')
def stock_history():
    action_filter = request.args.get('action')
    start_date = request.args.get('start')
    end_date = request.args.get('end')

    logs_query = InventoryLog.query

    if action_filter:
        logs_query = logs_query.filter(InventoryLog.action == action_filter)

    if start_date:
        try:
            start = datetime.strptime(start_date, "%Y-%m-%d")
            logs_query = logs_query.filter(InventoryLog.date >= start)
        except ValueError:
            flash("Data de início inválida.", "danger")

    if end_date:
        try:
            end = datetime.strptime(end_date, "%Y-%m-%d")
            logs_query = logs_query.filter(InventoryLog.date <= end)
        except ValueError:
            flash("Data de fim inválida.", "danger")

    logs = logs_query.order_by(InventoryLog.date.desc()).all()
    return render_template('stock.html', logs=logs)

@stock_bp.route('/adjust', methods=['GET', 'POST'])
def adjust_stock():
    products = Product.query.all()
    if request.method == 'POST':
        product_id = int(request.form['product_id'])
        action = request.form['action']  # entrada / saida / ajuste
        quantity = int(request.form['quantity'])
        note = request.form.get('note', '')

        product = Product.query.get(product_id)
        if not product:
            flash("Produto não encontrado.", "danger")
            return redirect(url_for('stock.adjust_stock'))

        if action == 'entrada':
            product.stock += quantity
        elif action in ['saida', 'ajuste']:
            if product.stock < quantity:
                flash("Estoque insuficiente.", "danger")
                return redirect(url_for('stock.adjust_stock'))
            product.stock -= quantity

        log = InventoryLog(
            product_id=product.id,
            action=action,
            quantity=quantity,
            date=datetime.utcnow(),
            note=note
        )

        db.session.add_all([product, log])
        db.session.commit()
        flash("Movimentação registrada com sucesso!", "success")
        return redirect(url_for('stock.stock_history'))

    return render_template('adjust_stock.html', products=products)
