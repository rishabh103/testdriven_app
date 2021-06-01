from flask import Blueprint, jsonify, request
from project.api.models import User
from project import db
import json
users_blueprint = Blueprint('users', __name__)

@users_blueprint.route('/users/ping', methods=['GET'])
def ping_pong():
    return jsonify({
    'status': 'success',
    'message': 'pong!'
    })

@users_blueprint.route('/users',methods=['POST'])
def add_user():
    post_data = request.get_json()
    username = post_data.get('username')
    email = post_data.get('email')
    db.session.add(User(username=username, email=email))
    db.session.commit()
    response_object = {
    'status': 'success',
    'message': f'{email} was added!'
    }
    return jsonify(response_object), 201


@users_blueprint.route('/users/<user_id>',methods=['GET'])
def get_single_user(user_id):
    """Get single user details"""
    user = User.query.filter_by(id=user_id).first()
    response_object = {
    'status': 'success',
    'data': {
    'id': user.id,
    'username': user.username,
    'email': user.email,
    'active': user.active
        }
    }
    return jsonify(response_object), 200

@users_blueprint.route('/users',methods=['GET'])
def get_all_user():
    """Get all user details"""

    
    
    response_object = {
    'status': 'success',
    'data': {
    'users': [user.to_json() for user in User.query.all()]
        }
    }
    return jsonify(response_object), 200