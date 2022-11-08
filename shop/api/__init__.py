from flask import Blueprint
from flask import jsonify
from ..models import now_utc

api = Blueprint('api', __name__, url_prefix='/api')

__version = '0.1'


@api.route('/')
@api.route('/health_check')
def health_check():
    status = 'good'
    return jsonify({'health_check': status, 'version': __version, 'server_time': now_utc()})


def __init__():
    from . import products


__init__()
