# 代表的な4つのデータ構造
# リスト　タプル　集合　辞書

# リスト インデックスやスライスが使用可能　要素の変更も可能
flavor = ["vanilla", "chocolate", "strawberry"]
flavor
# 異なる型の値を格納する事もできる
#　list関数を使用すると、繰り返し可能なオブジェクトからリストを作成できる
list(range(10)) # 0~9のリスト
list("ABCDEFG") # A~Gのリスト

# インデックスを使用して抽出もできる
flavor[0]
flavor[1:]
flavor[::2]

# リストの要素を変更する
flavor[2] = "mint" # 2番目の要素を入れ替えた
flavor

flavor[0:2] = ["バニラ", "チョコ"]
flavor

# 注意点
# 変数がメモリ上のオブジェクトを参照してデータを引っ張ってくる仕様上
# 同じオブジェクトを参照している片方の変数を使って値を変更した場合
# もう片方も同じオブジェクトを参照するために、リストの中身が変わってしまう。
# それを避けるために、スライスやcopyメソッドを使う
item = flavor[:] # スライスの手法
item = flavor.copy() # copyメソッド
item
id(flavor)
id(item)
# 別のリストを参照しているので、片方を変更しても、もう片方に影響はない。

# リストへの要素追加　方法は幾つもある
drink = [] # 空のリスト
drink.append("coffee") # appendメソッド
drink += ["tea"] # 累算代入文
drink.extend(["milk"]) # extendメソッド
drink[len(drink):] = ["water"] # スライスを用いた方法
drink
# リスト同士を結合する事もできる
drink2 = ["juice", "yakult"]
x = drink + drink2
x
y = drink
y += drink2 # すでに格納されている変数に足す方法もある
y

# リストの要素の削除方法
# インデックスを用いて削除する方法
del y[1] # del文
y
y.pop(2) # popメソッドは削除すると共に、削除した要素を戻り値として返す。
y
# 値から削除する方法
y.remove("milk")
y
# 範囲で削除する方法
del x[1:3] # del文を用いる方法
x
x[0:1] = [] # 空のリストを代入する方法
x

# リストの途中に挿入する方法
x.insert(1, "hotmilk") # insertメソッド
x
x[1:1] = ["tea", "coffee"] # スライスを用いる方法
x

# リストの全ての要素を削除
x.clear() # clearメソッド
x
# また変数に代入されている場合は
y = [] # 空のリストを代入して上書き 
y