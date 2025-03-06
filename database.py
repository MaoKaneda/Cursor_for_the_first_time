from models import db
from app import app

def init_db():
    """データベースを初期化する関数"""
    with app.app_context():
        db.create_all()
        print("データベースの初期化が完了しました") 