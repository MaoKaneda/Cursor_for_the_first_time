# ファイルに文字を書き込む関数
# file_path: 保存するファイルの場所（例：'input.txt'）
# text: 保存したい文字
def write_file(file_path, text):
    with open(file_path, 'w') as file:
        file.write(text)

# ファイルから文字を読み取る関数
# file_path: 読み取りたいファイルの場所
# 戻り値: ファイルの中身（文字列）
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# ファイルに文字を追加する関数
# file_path: 追加するファイルの場所
# text: 追加したい文字
def append_file(file_path, text):
    with open(file_path, 'a') as file:
        file.write(text)

# 文章を行ごとに分ける関数
# text: 分けたい文章
# 戻り値: 行ごとに分けられた文章のリスト
def parse_input(text):
    return text.split('\n')

# このファイルを直接実行した時だけ実行される部分
if __name__ == "__main__":
    # ユーザーからの入力をファイルに保存するプログラム
    # 空の行（何も入力せずにEnterキーを押す）まで続けて入力できる

    while True:
        # ユーザーから文字を入力してもらう
        user_input = input("Enter your text: ")
        # 入力された文字をファイルに追加
        append_file('input.txt', user_input)
        
        # 空の行が入力されたら終了
        if user_input == "":
            break

    # 処理が成功したことを表示
    print("File written successfully")
    # エラーが発生した場合の処理
    try:
        print("File written successfully")
    except IOError as e:
        # ファイルの読み書きに関するエラーが発生した場合
        print(f"エラーが発生しました: {e}")
    except Exception as e:
        # その他の予期せぬエラーが発生した場合
        print(f"予期せぬエラーが発生しました: {e}")
        # 静的ファイルを提供するための設定
        app.use(express.static('public'))

        