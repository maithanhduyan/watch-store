from datetime import datetime
from . import db
from flask import  url_for

class User(db.Model):
    # __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    def to_json(self):
        json_data = {
            'url': url_for('api.get_user', id=self.id, _external=True),
            'id': self.id,
            'username': self.username,
            'email': self.email,
        }
        return json_data

class Post(db.Model):
    # __tablename__='posts'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):
        return '<Post {}>'.format(self.body)
    
    def to_json(self):
        json_data = {
            'id': self.id,
            'body': self.body,
            'timestamp': self.timestamp,
            'user_id': url_for('api.get_user',id=self.user_id,_external=True),
        }
        return json_data