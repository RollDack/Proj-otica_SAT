from app import db
from app.models import Product, Sale

def test_create_product():
    product = Product(name="Lente de Contato", price=200.0, stock=50)
    db.session.add(product)
    db.session.commit()

    saved_product = Product.query.first()
    assert saved_product.name == "Lente de Contato"
    assert saved_product.price == 200.0
    assert saved_product.stock == 50