from flask import Flask
from flask_jwt_extended import JWTManager
from models import db
from auth import auth
import os
from datetime import timedelta

app = Flask(__name__)

# 設定
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'your-secret-key')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)

# データベースとJWTの初期化
db.init_app(app)
jwt = JWTManager(app)

# 認証ブループリントの登録
app.register_blueprint(auth)

if __name__ == '__main__':
    app.run(debug=True) 