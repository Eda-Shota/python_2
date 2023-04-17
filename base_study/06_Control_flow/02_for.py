# for文
# 一般的にforeach文と呼ばれ、each(それぞれ)野」要素に対して処理を適用するイメージ
for x in ["Mornig", "Afternon", "Evening", "Night"]:
    print("Good", x)

# 様々なイテラブルから要素を取り出す事が可能
# 文字列の場合
for a in "python":
    print(a)
# 一文字ずつ出力される

# リストの場合
meat = ["beef", "pork", "chicken"]
for b in meat:
    print(b)
# 要素が1つずつ出力される
#補足、for文の中でリストの要素に変更を加えようとすると予期せぬエラーが生じる
meat = ["beef", "pork", "chicken"]
for b in meat:
    if (b == "pork"):
        meat.remove(b)
    else:
        print(b)
# porkを除外する意図があったが、for文実行中は取りだした位置を記録しているため。
# 要素の変更が生じると、取り出した位置と実際のリストの状態が食い違う事がある
# それを避けるために、[:]スライスかcopyメソッドを使って、コピーを作成し
# そのコピーに対してfor文を適用すれば、影響は出ない
meat = ["beef", "pork", "chicken"]
for b in meat[:]:
    if (b == "pork"):
        meat.remove(b)
    else:
        print(b)
# 集合と辞書に対しても同様に、コピーを作ってfor文を適用させると良い

# タプルも同様に取り出せる
# 集合は、順番が追加順とは」限らない

# 辞書は順序通りにキーを取り出す事が出来る.
# また取り出したキーを利用して値を表示する事も可能。
meat = {"beef": 199, "pork": 99, "chicken": 49}
for c in meat:
    print(c, "is", meat[c], "yen")
# キーと値を同時に取り出す方法として、itemsメソッドもある。
meat = {"beef": 199, "pork": 99, "chicken": 49}
for c in meat.items(): # itemsメソッドを使用
    print(c)
# こうする事でタプルの型で取り出す事が出来る
# for文を利用したアンパッキングも可能
# タプル型で取り出したものを、アンパッキングする
meat = {"beef": 199, "pork": 99, "chicken": 49}
for name, price in meat.items():
    print(name, "is", price, "yen")

# range関数
# range(開始値、終了値、ステップ)と記述し、繰り返す範囲と間隔を指定できる。
for x in range(10):
    print(x, end=" ")
for x in range(10, 21):
    print(x, end=" ")
for x in range(21, 40, 3): # ナベアツ式
    print(x, end=" ")
# 終了値は値に含まれない事に注意
# rangeを用いた九九
for x in range(1, 10):
    for y in range(1, 10):
        print(x*y, end=" ")
    print()
# 補足、桁数を揃えて表示する方法
for x in range(1, 10):
    for y in range(1, 10):
        print(f"{x*y:2}", end=" ")
    print()

# enumerate関数
# 繰り返しの回数が分かる（何番目の繰り返しか）
drink = ["cofee", "tea", "juice"]
for i, x in enumerate(drink, 1): # ()内はイテラブル,開始値
    print(i, x)
# リストであればrange関数を利用して順番を表示する事も可能だが
# enumerateはインデックスが存在しないデータ型にも利用可能(集合等)
drink = {"cofee", "tea", "juice"}
for i, x in enumerate(drink, 1): # ()内はイテラブル,開始値
    print(i, x)

# reversed関数
# 逆順に取り出すことが出来る。
drink = ["cofee", "tea", "juice"]
for x in reversed(drink):
    print(x)
# enumerate関数と組み合わせる事もできるが、そのままでは逆順での取り出しに対応していないため、
# enumerateの戻り値をlist関数に渡してから逆順に取り出すなどの工夫が必要
drink = ["cofee", "tea", "juice"]
for i, x in reversed(list(enumerate(drink, 1))): 
    print(i, x)