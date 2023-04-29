# オブジェクトの生成や変換に使う関数

# ・既出のもの
# int(値) 整数
# float(値) 浮動小数点数
# str(値) 文字列
# bool(値) 真偽値
# list(イテラブル) リスト
# tuple(イテラブル) タプル
# set(イテラブル) 集合
# dict(イテラブル) 辞書

# bytes関数、bytearray関数
# 引数(文字列、整数、イテラブル、etc...)をバイト列やバイト配列に変換する。(整数の組み合わせに変換)
list(bytes("python", encoding="utf-8")) # bytes(文字列, encoding=文字エンコーディング)
list(bytes(123)) # bytes(整数)

# memoryview関数
# オブジェクトの内部にあるメモリーを操作するための関数。
# メモリのコピーを作らずに、元のメモリを操作できる
x = bytearray("python", encoding="utf-8")
y = memoryview(x) # xのメモリービューを作成しyに代入。
y[0] = 80 # 配列の0番目に、「P」の配列コードを挿入
x

# complex関数
# 複素数のオブジェクトを作成する
complex(1, 2) #complex(実部, 虚部)

# frozenset関数
# イミュータブルな集合のオブジェクトを生成する。（作成後に変更が出来ない）
{frozenset(("blue", "red")): "purple", frozenset(("red", "green")): "yellow"}

# object関数
# 全てのクラスにとっての基底クラスであるobjectオブジェクトを生成する
object()

# slice関数
# sliceの範囲を表すsliceオブジェクトを生成する
x = slice(10) # slice(終了値)
print(x.stop) # 終了値「10」が表示される

y = slice(10, 20, 3) # slice(開始値, 終了値, ステップ)
print(y.start, y.stop, y.step) # 開始値「10」終了値「20」ステップ「3」が表示される