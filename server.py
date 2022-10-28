from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+ os.path.join(basedir, 'database/watch-store.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
# initialize the app with the extension
db.init_app(app)

from routes import post

with app.app_context():
    db.create_all()

