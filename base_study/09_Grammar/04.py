# ラムダ式
# 無名関数を作成するための文法
# Lamda 引数, …: 式　という形で
# def 関数名(引数, …):
#     return 式　と同じ結果を得られる

def loop(f): # 0から９までを繰り返すloop関数
    for i in range(10):
        print(f(i), end=" ")

# 例:ラムダ式を使わない場合
def square(x): # 引数の2条を返す
    return x*x

loop(square) # 九九の二乗の部分を表示する

# 例:ラムダ式を使った場合
loop(lambda x: x*x) # 三行に渡ったコードが一行に
# 無名であるため、何の式か分かりづらく、繰り返し呼び出す場合は通常の式の方がトータルで短くなるが
# 一度しか使わない場合は、ラムダ式の方が簡潔。

# ソート
# 複数のデータを決まった方式で並べ直す。
# sorted関数を使う場合
menu = [("burger", 110, 234), ("potato", 150, 226), ("shake", 120, 218)]
sorted(menu, reverse=True) # sorted(イテラブル)の形、第二引数にreverse~Trueを記述する事で逆順になる。
# sortメソッドを使う場合
# リスト.sort()
# sortメソッドはリストにしか使えない。
# 一方、sorted関数はリスト以外にも使える

#キーを指定して並べ替えす
sorted(menu, key=lambda x: x[1]) # この場合、タプルの一番目の要素を戻り値として返し、その順番で並び替える(今回の場合は値段)
sorted(menu, key=lambda x: x[2], reverse=True) # カロリーの逆順
sorted(menu, key=lambda x: x[2]/x[1], reverse=True) # 価格あたりのカロリー逆順とかも可能