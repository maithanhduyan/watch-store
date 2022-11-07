# -*- coding: utf-8 -*-

from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy

# App
app = Flask(__name__)
app.config.from_object(Config)

# Database
db = SQLAlchemy()
def init_database():
    db.init_app(app)
    from . import models
    return

with app.app_context():
    init_database()
    from .api import api
    app.register_blueprint(api, url_prefix='/api')
    from . import views