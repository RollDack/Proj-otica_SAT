from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sua_chave_secreta_aqui'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:password@localhost/optical_store'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from app.routes.home import home_bp
    from app.routes.customer import customers_bp
    from app.routes.products import products_bp
    from app.routes.sales import sales_bp
    from app.routes.employees import employee_bp
    from app.routes.catalog import catalog_bp
    from app.routes.cart import cart_bp
    from app.routes.appointments import appointments_bp
    from app.routes.stock import stock_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(customers_bp, url_prefix='/customers')
    app.register_blueprint(products_bp, url_prefix='/products')
    app.register_blueprint(sales_bp, url_prefix='/sales')
    app.register_blueprint(employee_bp, url_prefix='/employee')
    app.register_blueprint(catalog_bp, url_prefix='/catalog')
    app.register_blueprint(cart_bp, url_prefix='/cart')
    app.register_blueprint(appointments_bp, url_prefix='/appointments')
    app.register_blueprint(stock_bp, url_prefix='/stock')

    return app