import json
from flask import request, jsonify
from src.app import app, db
from src.models import User
from src.utils import generate_jwt, verify_password, hash_password
from sqlalchemy.exc import IntegrityError

@app.route('/register/', methods=['POST'])
def register_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    if not username or not password or not email:
        return jsonify({"message": "Username, password, and email are required"}), 400
    
    try:
        new_user = User(username=username, password=password, email=email)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User registered successfully"}), 201
    except IntegrityError:
         db.session.rollback()
         return jsonify({"message": "Username or email already taken."}), 409

@app.route('/login/', methods=['POST'])
def login_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({"message": "Username and password are required"}), 400
    
    user = User.query.filter_by(username=username).first()
    if user and verify_password(password, user.password):
        token = generate_jwt({'user_id': user.id, 'username': user.username})
        return jsonify({'token': token}), 200
    else:
        return jsonify({"message": "Invalid username or password"}), 401

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'created_at': user.created_at,
            'updated_at': user.updated_at
        }), 200
    else:
        return jsonify({"message": "User not found"}), 404

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404

    data = request.get_json()
    user.username = data.get('username', user.username)
    user.email = data.get('email', user.email)

    if data.get('password'):
        user.password = hash_password(data.get('password'))

    db.session.commit()
    return jsonify({"message": "User updated successfully"}), 200

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted successfully"}), 200
    else:
        return jsonify({"message": "User not found"}), 404