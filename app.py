# 必要なライブラリをインポート（他のプログラムの部品を取り込む）
from flask import Flask
from flask_jwt_extended import JWTManager
from auth import auth
from database import setup_db
import os
from datetime import timedelta

def create_app():
    """Webアプリケーションを作成する関数"""
    # Flaskアプリケーションを新しく作る
    app = Flask(__name__)
    
    # ログイン機能のための秘密鍵を設定
    # 環境変数から取得するか、なければ'your-secret-key'を使う
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'your-secret-key')
    # ログイン状態を1時間で切れるように設定
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)
    
    # データベースの設定を行う
    setup_db(app)
    
    # ログイン機能を使えるようにする
    jwt = JWTManager(app)
    
    # ログインや会員登録の機能をアプリケーションに追加
    app.register_blueprint(auth)
    
    return app

# アプリケーションを作成
app = create_app()

# このファイルを直接実行したときの処理
if __name__ == '__main__':
    # デバッグモードでアプリケーションを起動
    app.run(debug=True) 