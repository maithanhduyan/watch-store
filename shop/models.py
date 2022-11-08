# -*- coding: utf-8 -*-

from datetime import datetime
from datetime import timezone
from . import db

def now_utc():
    return datetime.now(timezone.utc)

class ProductCategory(db.Model):
    __tablename__ = 'product_categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    note = db.Column(db.String(100), nullable=True)

    def to_json(self):
        json_data = {
            'id': self.id,
            'name': self.name,
            'note': self.note,
        }
        return json_data


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    barcode = db.Column(db.String(120), index=True, unique=True)
    link = db.Column(db.String(1200))
    cost = db.Column(db.Float)
    sale_off = db.Column(db.Float)
    price = db.Column(db.Float)
    images = db.Column(db.String(190))

    def to_json(self):
        json_data = {
            'id': self.id,
            'name': self.name,
            'barcode': self.barcode,
            'cost': self.cost,
            'sale_off': self.sale_off,
            'price': self.price,
            'images': self.images,
        }
        return json_data
