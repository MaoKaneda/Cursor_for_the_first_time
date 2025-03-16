from app import create_app
from database import init_db

if __name__ == '__main__':
    app = create_app()
    init_db(app)
    print("データベースの初期化が完了しました") 