from ..models import  Post,User
from flask import  jsonify
from . import api


@api.route('/posts/')
def get_post():
    posts = Post.query.all()
    return jsonify({'posts': [post.to_json() for post in posts]})

@api.route('/users/<int:id>')
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify( user.to_json())
