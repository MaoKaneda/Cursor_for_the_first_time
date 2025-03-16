from flask import Flask
from models import db

def init_db(app: Flask):
    """
    データベースを初期化する関数
    
    Args:
        app: Flaskアプリケーションインスタンス
    """
    with app.app_context():
        db.create_all()
        print("データベースの初期化が完了しました")

def setup_db(app: Flask):
    """
    データベースの設定を行う関数
    
    Args:
        app: Flaskアプリケーションインスタンス
    """
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/users.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app) 