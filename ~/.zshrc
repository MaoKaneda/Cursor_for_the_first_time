# 数字を入力してもらう
number = int(input("数字を入力してください: "))

# 入力された数字が偶数か奇数かを判断する
if number % 2 == 0:  # %は割り算の余りを計算します
    # 偶数の場合の処理
    print(f"{number}は偶数です！")  # 例：2,4,6,8など
else:
    # 奇数の場合の処理
    print(f"{number}は奇数です！")  # 例：1,3,5,7など

# リストの例
fruits = ["りんご", "みかん", "バナナ"]  # リストに果物の名前を入れる

# forループを使って、リストの中身を1つずつ表示する
for fruit in fruits:  # fruitsリストの中身を1つずつfruitという変数に入れる
    print(f"私は{fruit}が好きです！")  # 順番に表示される

# プログラムの目的や概要をここに書く
def calculate_total(items):
    # 合計金額を保存する変数を初期化
    total = 0
    
    # 商品リストをループで処理
    for item in items:
        # 各商品の価格を合計に加算
        total += item.price
    
    # 最終的な合計金額を返す
    return total 