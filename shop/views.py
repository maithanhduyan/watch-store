from flask import render_template
from . import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/products')
def products():
    return render_template('products.html', title='Products')


@app.route('/product-details')
def product_details():
    return render_template('product-details.html', title='Product Details')


@app.route('/blog')
def blog():
    return render_template('blog.html', title='Blog')


@app.route('/blog-details')
def blog_details():
    return render_template('blog-details.html', title='Blog Details')


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')

@app.route('/terms-conditions')
def terms_conditions():
    return render_template('terms-conditions.html', title='Terms of Conditions')

@app.route('/privacy-policy')
def privacy_policy():
    return render_template('privacy-policy.html', title='Privacy Policy')


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template('errors/500.html'), 500
