# ファイルの読み書きを行うための関数をまとめたファイル
# これは、ノートに文字を書いたり、ノートから文字を読んだりする作業に似ています

def write_file(file_path, text):
    """
    ファイルに文字を書き込む関数（新しいノートに文字を書くようなもの）
    
    Args:
        file_path: ノートの場所（例：'input.txt'）
        text: 書きたい内容
    
    使い方：
    write_file('メモ.txt', 'こんにちは！')
    → 「メモ.txt」というファイルに「こんにちは！」と書き込まれます
    """
    with open(file_path, 'w') as file:  # ノートを開く
        file.write(text)                 # 文字を書く

def read_file(file_path):
    """
    ファイルから文字を読み取る関数（ノートの内容を読むようなもの）
    
    Args:
        file_path: 読みたいノートの場所
    Returns:
        ノートの中身（文字列）
    
    使い方：
    内容 = read_file('メモ.txt')
    → 「メモ.txt」の中身を読み取って「内容」に保存
    """
    with open(file_path, 'r') as file:  # ノートを開く
        return file.read()              # 中身を読む

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

        