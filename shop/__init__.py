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


@click.command('db-create-all')
def db_create_all_command():
    """Clear the existing data and create new tables."""
    db.create_all()
    click.echo('Created All Tables')


@click.command('db-drop-all')
def db_drop_all_command():
    """Drop all tables."""
    db.drop_all()
    click.echo('Drop All Tables')


@click.command('db-insert-data-sample')
def db_insert_data_sample_command():
    """Data Sample"""
    db_create_all_command()

    click.echo('Drop All Tables')


def db_command():
    app.cli.add_command(db_create_all_command)
    app.cli.add_command(db_drop_all_command)


with app.app_context():
    init_database()
    db_command()
    from .api import api
    from .auth import auth
    app.register_blueprint(api)
    app.register_blueprint(auth)
    # make "index" point at "/", which is handled by "blog.index"
    app.add_url_rule("/", endpoint="index")
    from . import views
