# 必要なツールを集める
# データベースを使うための道具（本棚を管理するための道具）
from flask_sqlalchemy import SQLAlchemy
# パスワードを暗号化するための道具（秘密の暗号を作る道具）
from werkzeug.security import generate_password_hash, check_password_hash

# データベース（本棚）を用意する
db = SQLAlchemy()

# ユーザー情報を管理するための設計図
class User(db.Model):
    """
    ユーザーの情報を保存するための箱
    これは図書館のカード（利用者カード）のようなもの
    """
    # ユーザーごとの番号（図書館の利用者番号みたいなもの）
    # primary_Trueは「この番号は一人一人違う」という意味
    id = db.Column(db.Integer, primary_key=True)
    
    # ユーザー名（あだ名みたいなもの）
    # unique=Trueは「同じ名前は使えない」という意味
    # nullable=Falseは「必ず入力が必要」という意味
    username = db.Column(db.String(80), unique=True, nullable=False)
    
    # メールアドレス（連絡先）
    # 同じく重複禁止で必須項目
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    # パスワード（暗号化して保存）
    # 暗号化とは「abc123」という文字を「x#k9$p」のように変換すること
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        """
        パスワードを安全な形に変換して保存する関数
        （普通の文字を暗号に変換する）
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """
        入力されたパスワードが正しいか確認する関数
        （暗号を解読して、合っているか確認する）
        """
        return check_password_hash(self.password_hash, password) 