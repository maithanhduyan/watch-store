from datetime import datetime
from . import db

class ProductCategory(db.Model):
    __tablename__='product_categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    note = db.Column(db.String(100), nullable=True)

class Product(db.Model):
    __tablename__='products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    barcode = db.Column(db.String(120), index=True, unique=True)
    link = db.Column(db.String(1200))
    cost = db.Column(db.Float)
    sale_off = db.Column(db.Float)
    price = db.Column(db.Float)
    images = db.Column(db.String(190))
