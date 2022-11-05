import os 

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '!@#$%^&*12345678'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False
    SQLALCHEMY_RECORD_QUERIES = True
    FLASKY_DB_QUERY_TIMEOUT = 0.5
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:123@localhost/flask' or 'sqlite:///'+os.path.join(basedir,'blog.db')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_SERVER = 'smtp.google.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    FLASKY_MAIL_SENDER = "Blog Admin <540918220@google.com>"
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN') or '540918220@google.com'
    FLASKY_MAIL_SUBJECT_PREFIX = '[Blog]'
    DEBUG = True