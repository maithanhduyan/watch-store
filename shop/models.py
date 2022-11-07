from datetime import datetime
from . import db

class Product(db.Model):
    # __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    barcode = db.Column(db.String(120), index=True, unique=True)
    link = db.Column(db.String(1200))
