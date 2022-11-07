from flask import render_template
from . import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('errors/500.html'), 500