from flask import Blueprint, jsonify

users_blueprint = Blueprint('users', __name__)

@users_blueprint.route('/users/hello', methods=['GET'])
def hello_hi():
    return jsonify({
        'status': 'success',
        'message': 'hi you!'
    })
