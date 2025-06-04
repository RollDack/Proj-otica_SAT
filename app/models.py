from app import db
from sqlalchemy.orm import validates
from datetime import datetime

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    phone = db.Column(db.String(20))
    birthdate = db.Column(db.Date)


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(14), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    birthdate = db.Column(db.Date, nullable=False)
    position = db.Column(db.String(50), nullable=False)
    salary = db.Column(db.Float, nullable=False)
    access_key = db.Column(db.String(50), unique=True, nullable=False)
    boss_position = db.Column(db.Boolean, default=False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.boss_position = self.access_key.endswith("A-01")

    @validates('access_key')
    def validate_access_key(self, key, value):
        self.boss_position = value.endswith("A-01")
        return value



class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=True)
    quantity = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(100), nullable=True)

    product = db.relationship("Product")

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    description = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), default='Pendente')
    

    customer = db.relationship('Customer', backref='appointments')
    employee = db.relationship('Employee', backref='appointments')

class InventoryLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    action = db.Column(db.String(50), nullable=False)  # 'entrada', 'saida', 'ajuste'
    quantity = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    note = db.Column(db.String(255))

    product = db.relationship('Product', backref='inventory_logs')
