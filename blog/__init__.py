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


def init_api():
    from .api import api as api_v1
    app.register_blueprint(api_v1, url_prefix='/api')
    return 0


def init_views():
    from . import views
    return


with app.app_context():
    init_database()
    db.create_all()
    init_api()
    init_views()
