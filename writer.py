# ファイルの読み書きを行うための関数をまとめたファイル

def write_file(file_path, text):
    """
    ファイルに文字を書き込む関数
    
    Args:
        file_path: 保存するファイルの場所（例：'input.txt'）
        text: 保存したい文字
    """
    with open(file_path, 'w') as file:
        file.write(text)

def read_file(file_path):
    """
    ファイルから文字を読み取る関数
    
    Args:
        file_path: 読み取りたいファイルの場所
    Returns:
        ファイルの中身（文字列）
    """
    with open(file_path, 'r') as file:
        return file.read()

def append_file(file_path, text):
    """
    既存のファイルに文字を追加する関数
    
    Args:
        file_path: 追加するファイルの場所
        text: 追加したい文字
    """
    with open(file_path, 'a') as file:
        file.write(text)

def parse_input(text):
    """
    文章を行ごとに分ける関数
    
    Args:
        text: 分けたい文章
    Returns:
        行ごとに分けられた文章のリスト
    """
    return text.split('\n')

# このファイルを直接実行した時の処理
if __name__ == "__main__":
    # 無限ループでユーザーからの入力を受け付ける
    while True:
        # ユーザーから文字を入力してもらう
        user_input = input("Enter your text: ")
        # 入力された文字をファイルに追加
        append_file('input.txt', user_input)
        
        # 空の入力があったらループを終了
        if user_input == "":
            break

    # エラーが発生する可能性のある処理
    try:
        print("File written successfully")
    except IOError as e:
        # ファイルの読み書きでエラーが発生した場合
        print(f"エラーが発生しました: {e}")
    except Exception as e:
        # その他の予期せぬエラーが発生した場合
        print(f"予期せぬエラーが発生しました: {e}")

        