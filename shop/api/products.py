from ..models import  Product,ProductCategory
from flask import  jsonify
from . import api


@api.route('/products/', methods=['GET', 'POST'])
def get_all_products():
    products = Product.query.all()
    return jsonify({'products': [product.to_json() for product in products]})