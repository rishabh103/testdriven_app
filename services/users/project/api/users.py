from flask import Blueprint, jsonify, request
from project.api.models import User
from project.tests.utils import add_user
from project import db
import json, jwt
users_blueprint = Blueprint('users', __name__)

@users_blueprint.route('/users/ping', methods=['GET'])
def ping_pong():
    return jsonify({
    'status': 'success',
    'message': 'pong!'
    })

@users_blueprint.route('/users',methods=['POST'])
def add_user1():
    post_data = request.get_json()
    username = post_data.get('username')
    email = post_data.get('email')
    password = post_data.get('password')
    db.session.add(User(username=username, email=email, password=password))
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
    'active': user.active,
    'password':user.password
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


@users_blueprint.route('/users/test',methods=['POST'])
def getTestUser():
    post_data = request.get_json()
    user = add_user('justatest', 'test@test.com', 'test')
    auth_token = user.encode_auth_token(user.id)
    print(auth_token, flush=True)
    # auth_token = bytes(auth_token, 'utf-8')
    print(type(auth_token), flush=True)
    print((user.decode_auth_token(auth_token), user.id), flush=True)
    response_object = {
    'status': 'success',
    'message': 'was added!'
    }
    return jsonify(response_object), 201