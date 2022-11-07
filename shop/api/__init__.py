from flask import Blueprint
from flask import  jsonify

api  = Blueprint('api', __name__)

@api.route('/')
@api.route('/health_check')
def health_check():
    return jsonify({'healthCheck': 'good'})