# 必要なツールを集める（料理で言えば、必要な調理器具を集めるようなもの）
from flask import Flask  # Webアプリを作るための主要な道具
from flask_jwt_extended import JWTManager  # ログイン機能を作るための道具
from auth import auth  # ユーザー登録とログインの機能
from database import setup_db  # データベース（情報を保存する倉庫）の設定
import os  # パソコンの設定を読み取るための道具
from datetime import timedelta  # 時間を計算するための道具

def create_app():
    """
    Webアプリケーションを作る関数
    （お店を開くための準備をするようなもの）
    """
    # お店（Webアプリ）を新しく開く
    app = Flask(__name__)
    
    # ログインのための特別な鍵を設定
    # （お店の鍵のようなもの。これがないと安全に開けない）
    # 環境設定から鍵を探して、なければ仮の鍵を使う
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'your-secret-key')
    
    # ログイン状態の有効期限を1時間に設定
    # （1時間たったら、もう一度ログインが必要）
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)
    
    # データベース（お客さんの情報を保存する本棚）の設定
    setup_db(app)
    
    # ログインシステムを使えるようにする
    # （入館証を確認する警備員さんを配置するようなもの）
    jwt = JWTManager(app)
    
    # ログインと会員登録の機能をアプリに追加
    # （受付係さんを配置するようなもの）
    app.register_blueprint(auth)
    
    return app

# お店（Webアプリ）を実際に作る
app = create_app()

# このプログラムを直接実行したときの処理
if __name__ == '__main__':
    # お店を開く（デバッグモードで起動）
    # デバッグモードとは、問題が起きたときに詳しく教えてくれるモード
    app.run(debug=True) 