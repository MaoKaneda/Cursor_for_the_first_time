from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models import db, User

auth = Blueprint('auth', __name__)

@auth.route('/users/signup', methods=['POST'])
def signup():
    data = request.get_json()
    
    if not data or not data.get('username') or not data.get('email') or not data.get('password'):
        return jsonify({'error': '必要な情報が不足しています'}), 400
    
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'error': 'このユーザー名は既に使用されています'}), 400
    
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'このメールアドレスは既に登録されています'}), 400
    
    user = User(
        username=data['username'],
        email=data['email']
    )
    user.set_password(data['password'])
    
    db.session.add(user)
    db.session.commit()
    
    return jsonify({'message': 'ユーザー登録が完了しました'}), 201

@auth.route('/users/login', methods=['POST'])
def login():
    data = request.get_json()
    
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'error': 'ユーザー名とパスワードが必要です'}), 400
    
    user = User.query.filter_by(username=data['username']).first()
    
    if user and user.check_password(data['password']):
        access_token = create_access_token(identity=user.id)
        return jsonify({
            'access_token': access_token,
            'message': 'ログインに成功しました'
        }), 200
    
    return jsonify({'error': 'ユーザー名またはパスワードが間違っています'}), 401

@auth.route('/users/me', methods=['GET'])
@jwt_required()
def get_current_user():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    
    return jsonify({
        'id': user.id,
        'username': user.username,
        'email': user.email
    }), 200 