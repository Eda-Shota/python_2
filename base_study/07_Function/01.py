# 引数　
# 位置引数とキーワード引数がある。
print("Hello", "Python", end="")
# "Hello"等が位置引数、end=""がキーワード引数。

def order(main, side, drink): # order関数の定義
    print("main :", main)
    print("side :", side)
    print("drink :", drink)

order("steak", "salad", "coffee") # order関数の呼び出し

# 仮引数...関数の定義に記述する引数のこと
# 実員数...関数を呼び指すときに引き渡す引数

# return文
# 関数から戻り値を返す
def odd_even(n): # odd_even関数の定義
    return "odd" if n%2 else "even" # 0はFalseの扱い

print(odd_even(5)) # odd_even関数の呼び出し(引き数は5)
print(odd_even(6)) # odd_even関数の呼び出し(引き数は6)

# return文は関数の途中に記載する事も可能。
def odd_even(n):
    if n != int(n):
        return "error" # この文が実行されれば、下の文が実行されずに値を返す
    return "odd" if n%2 else "even" # 上の文が実行されていなければ、実行される

print(odd_even(5))
print(odd_even(6))
print(odd_even(7.7))

# 位置引数の順序
# 仮引数と実引数の順序を合わせる必要がある。
def order(main, side, drink)
    print("main :", main)
    print("side :", side)
    print("drink :", drink)

order("pizza", "soup", "juice")
# pizzaがmain、soupがside、juiceがdrinkに代入される。

# *を使って、実引数に「*イテラブル」のように記述すると、
# イテラブルの各要素を別々の引数として冠すに割らすことが出来る
# イテラブルアンパッキングと呼ばれる。
def order(main, side, drink):
    print("main :", main)
    print("side :", side)
    print("drink :", drink)

snack = ["hotcake", "fruit", "tea"]
order(*snack)

snack2 = ["hotcake", "fruit"]
order(*snack2, "tea")
# この二つの呼び出しは同様の結果が得られる

# キーワード引数の順序
# 仮引数と実引数の順序は合わせる必要が無い。
order(main="steak", side="salad", drink="coffee")
order(side="salad", drink="coffee", main="steak")
order(drink="coffee", main="steak", side="salad")
# どれも同じ結果が得られる

# 位置引数とキーワード引数を併用する場合は、位置引数を左に
# キーワード引数を右に置く。
order("steak", drink="coffee", side="salad")
# キーワード引数を左に置くとエラーが発生する

# *を2個使って、実引数に「**辞書」と記述すると
# 「キー＝値」というキーワード引数として関数に渡す事が出来る
# 辞書アンパッキングと言う。
# 通常の引数と混ぜて使用したり、複数回使用する事もできる。
dessert = {"main": "parfait", "side": "cookie", "drink": "cocoa"}
order(**dessert) # 上述のコードと同様の結果が得られる

#イテラブルアンパッキングと辞書アンパッキングを併用する倍、前者を左に、後者を右に置く
order("hotcake", *["fruit"], **{"drink": "tea"}) # 位置引数やイテラブルが左にある
order(*["parfait"], **{"drink": "cocoa"}, side="cookie") # イテラブルを左に、辞書やキーワード引数が右に

# 引数にはデフォルト値が設定できる
def order(main="steak", side="salad", drink="coffee"): # デフォルト値を設定している
    print("main :", main)
    print("side :", side)
    print("drink :", drink)

order() # 全てデフォルト値で返す
order("pizza") # 一番目の要素をpizza、他をデフォルト値で返す
order(side="soup") # sideのキーワードを持つ要素の値をsoupで返す。