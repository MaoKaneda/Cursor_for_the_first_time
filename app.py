from flask import Flask
from flask_jwt_extended import JWTManager
from auth import auth
from database import setup_db
import os
from datetime import timedelta

def create_app():
    """アプリケーションファクトリ関数"""
    app = Flask(__name__)
    
    # JWT設定
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'your-secret-key')
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)
    
    # データベース設定
    setup_db(app)
    
    # JWTの初期化
    jwt = JWTManager(app)
    
    # 認証ブループリントの登録
    app.register_blueprint(auth)
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True) 