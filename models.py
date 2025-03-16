# データベースを使うためのライブラリをインポート
from flask_sqlalchemy import SQLAlchemy
# パスワードを安全に保存するためのライブラリをインポート
from werkzeug.security import generate_password_hash, check_password_hash

# データベースの設定
db = SQLAlchemy()

# ユーザー情報を管理するクラス
class User(db.Model):
    # ユーザーごとの固有のID
    id = db.Column(db.Integer, primary_key=True)
    # ユーザー名（重複禁止、必須項目）
    username = db.Column(db.String(80), unique=True, nullable=False)
    # メールアドレス（重複禁止、必須項目）
    email = db.Column(db.String(120), unique=True, nullable=False)
    # パスワード（ハッシュ化して保存）
    password_hash = db.Column(db.String(128))

    # パスワードを安全な形式に変換して保存する関数
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # 入力されたパスワードが正しいかチェックする関数
    def check_password(self, password):
        return check_password_hash(self.password_hash, password) 