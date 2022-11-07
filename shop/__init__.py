# -*- coding: utf-8 -*-

from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
import click


# App
app = Flask(__name__)
app.config.from_object(Config)

# Database
db = SQLAlchemy()


def init_database():
    db.init_app(app)
    from . import models
    return


def db_command():
    """Clear the existing data and create new tables."""
    app.cli.add_command(db_create_all_command)


@click.command('db_create_all')
def db_create_all_command():
    """Clear the existing data and create new tables."""
    db.create_all()
    click.echo('Created All Tables')


with app.app_context():
    # Database
    init_database()
    db_command()

    #
    from .api import api
    app.register_blueprint(api, url_prefix='/api')
    from . import views
