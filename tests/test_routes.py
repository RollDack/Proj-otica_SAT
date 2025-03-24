import pytest
from app import create_app, db
from app.models import Product, Sale

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert "Loja de Ótica" in response.data

def test_add_product(client):
    response = client.post('/products/add', data={
        'name': 'Óculos de Sol',  # Palavras com acento estão OK agora
        'price': 150.50,
        'stock': 20
    }, follow_redirects=True)

    assert response.status_code == 200
    assert 'Óculos de Sol' in response.data

def test_delete_product(client):
    # Adicionar um produto
    response = client.post('/products/add', data={
        'name': 'Óculos de Teste',
        'price': 199.99,
        'stock': 10
    })
    assert response.status_code == 302  # Redirecionado após adição

    # Deletar o produto
    product = Product.query.filter_by(name='Óculos de Teste').first()
    response = client.post(f'/products/delete/{product.id}')
    assert response.status_code == 302  # Redirecionado após exclusão
