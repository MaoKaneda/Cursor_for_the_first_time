from flask import Flask
from models import db

def init_db(app: Flask):
    """
    データベース（本棚）を新しく作る関数
    
    Args:
        app: Webアプリケーション（お店全体）
    
    これは新しい図書館を開館するときのように、
    本棚を組み立てて、整理する作業に似ています。
    """
    with app.app_context():
        db.create_all()
        print("データベースの初期化が完了しました")

def setup_db(app: Flask):
    """
    データベース（本棚）の設定を行う関数
    
    Args:
        app: Webアプリケーション（お店全体）
    
    これは本棚をどこに置くか、どんな順番で本を並べるかなどを
    決めるような作業です。
    """
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/users.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app) 