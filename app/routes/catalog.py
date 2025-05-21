from flask import Blueprint, render_template
from app.models import Product

catalog_bp = Blueprint('catalog', __name__)

@catalog_bp.route('/')
def show_catalog():
    products = Product.query.all()
    return render_template('catalog.html', products=products)
