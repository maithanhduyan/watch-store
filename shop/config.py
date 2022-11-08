# -*- coding: utf-8 -*-

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '!@#$%^&*12345678'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123@localhost/watch' or 'sqlite:///' + os.path.join(basedir, 'watch.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASKY_DB_QUERY_TIMEOUT = 0.5

    # Upload file
    MAX_CONTENT_LENGTH = 16 * 1000 * 1000
    UPLOAD_FOLDER = os.path.join(basedir, 'uploads')
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

class ProductionConfig(Config):
    DATABASE_URI = 'postgresql://postgres:123@localhost/watch'

class DevelopmentConfig(Config):
    DATABASE_URI = os.path.join(basedir, 'watch.db')

class TestingConfig(Config):
    DATABASE_URI = 'sqlite:///:memory:'
    TESTING = True