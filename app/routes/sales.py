from flask import Blueprint, render_template, request
from app.models import db, Sale

sales_bp = Blueprint('sales', __name__)

@sales_bp.route('/')
def list_sales():
    sales = Sale.query.all()
    return render_template('sales.html', sales=sales)