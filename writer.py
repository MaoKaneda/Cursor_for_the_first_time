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
    ※注意：この関数を使うと、前に書いてあった内容は消えてしまいます
    """
    # ノートを「書く」モード('w')で開く
    # withを使うと、書き終わった後に自動でノートが閉じられる
    with open(file_path, 'w') as file:  
        # 文字を書く（前の内容は消える）
        file.write(text)                 

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
    
    例：
    もしメモ.txtに「こんにちは！」と書いてあれば、
    内容 = read_file('メモ.txt')とすると、
    内容という箱の中に「こんにちは！」が入ります
    """
    # ノートを「読む」モード('r')で開く
    with open(file_path, 'r') as file:  
        # 中身を全部読んで返す
        return file.read()              

def append_file(file_path, text):
    """
    既存のファイルに文字を追加する関数
    （ノートの最後のページに新しく文字を書き足すようなもの）
    
    Args:
        file_path: 追加するファイルの場所（例：'日記.txt'）
        text: 追加したい文字
    
    使い方：
    append_file('日記.txt', '今日は晴れでした')
    → 「日記.txt」の最後に「今日は晴れでした」が追加されます
    ※前に書いてあった内容は消えません！
    """
    # ノートを「追加」モード('a')で開く
    # 'a'はappend（追加）の略
    with open(file_path, 'a') as file:
        # 最後に文字を追加
        file.write(text)

def parse_input(text):
    """
    文章を行ごとに分ける関数
    （長い文章を、改行されているところで区切るような作業）
    
    Args:
        text: 分けたい文章
    Returns:
        行ごとに分けられた文章のリスト
    
    使い方：
    text = "1行目\n2行目\n3行目"
    結果 = parse_input(text)
    → 結果 = ["1行目", "2行目", "3行目"] となります
    """
    # \nは「改行」を表す特別な文字
    return text.split('\n')

# このファイルを直接実行した時の処理
# （このファイルを直接実行したときだけ動く部分）
if __name__ == "__main__":
    # 無限ループでユーザーからの入力を受け付ける
    # （ユーザーが終了を指示するまで続ける）
    while True:
        # ユーザーから文字を入力してもらう
        # 入力された文字はuser_inputという箱に保存される
        user_input = input("Enter your text: ")
        
        # 入力された文字をファイルに追加
        # 前の内容は消えずに、最後に追加される
        append_file('input.txt', user_input)
        
        # もし何も入力せずにEnterキーを押したら
        # （つまり、空の文字列が入力されたら）
        if user_input == "":
            # ループを終了する
            break

    # エラーが起きる可能性のある処理を試してみる
    # （料理で言えば、新しいレシピを試すようなもの）
    try:
        # 正常に終了したことを表示
        print("File written successfully")
    except IOError as e:
        # ファイルの読み書きでエラーが起きた場合
        # （例：ファイルが見つからない、権限がないなど）
        print(f"エラーが発生しました: {e}")
    except Exception as e:
        # その他の予期せぬエラーが起きた場合
        # （何が起きるか分からない場合の保険のようなもの）
        print(f"予期せぬエラーが発生しました: {e}")

        


        