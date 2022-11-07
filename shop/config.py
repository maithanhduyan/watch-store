import os 

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '!@#$%^&*12345678'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    FLASKY_DB_QUERY_TIMEOUT = 0.5
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:123@localhost/watch' or 'sqlite:///'+os.path.join(basedir,'watch.db')
    SQLALCHEMY_TRACK_MODIFICATIONS=False