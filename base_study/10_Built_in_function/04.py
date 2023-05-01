# イテラブルに対して適用する関数

# len関数　オブジェクトの長さ（要素数）を返します。
# len(オブジェクト)

# range 正確にはクラス rangeオブジェクトを生成して返す
# range(終了値)
# range(開始値, 終了値) 終了値-1まで1ずつ増加
# range(開始値, 終了値, ステップ)　ステップずつ変化

# enumerate関数 何番目に取り出した要素なのか、取り出した要素の値を返す。
# enumerate(イテラブル)
# enumerate(イテラブル, 開始値)　開始値を指定する

# reversed関数 イテラブルを逆順に取り出す
# reversed(イテラブル)

# zip関数
# 複数のイテラブルに対して同時に繰り返しを行いたい時に使用する。
name = ["burger", "potato", "shake"]
price = [110, 150, 120]
for n, p in zip(name, price): # zip(イテラブル, …)
    print(n, "is", p, "yen")

# map関数
# イテラブルが含むすべての要素に対して、指定した関数を適用するために使う
list(map(len, ["apple", "banana", "coconut"])) # map(関数, イテラブル, …)
# すべての要素の文字数を数えている

# filter関数
# イテラブルが含む要素の中から、特定の条件を満たす要素だけを抽出するために使います
list(filter(len, ["", "apple", "banana", "", "coconut", ""])) # filter(関数, イテラブル)
# filterによってFalse以外の要素が抽出される

# all関数
# イテラブルの要素全てがTrueならTrueを返す
all(x >= 80 for x in [90, 95, 80, 100, 85]) # all(イテラブル) Trueを返す
all(x >= 80 for x in [90, 75, 80, 100, 85]) # all(イテラブル) Falseを返す

# any関数
# イテラブルの要素のいずれかがTrueならTrueを返す
any(x >= 50 for x in [90, 45, 80, 100, 85]) # any(イテラブル) Trueを返す
any(x >= 50 for x in [90, 75, 80, 100, 85]) # any(イテラブル) Trueを返す

# iter関数 next関数
# イテレータはイテラブルなオブジェクトから要素を一個ずつ取り出す為のオブジェクト
# iterは指定されたイテラブルに対するイテレータを返す
# nextは指定されたイテレータから要素を一個取り出す
i = iter([1, 2, 3])
next(i) # 最初の要素が取り出される
next(i) # 次の要素をが取り出される
next(i) # さらに次の要素をが取り出される
next(i) # もう取り出す要素が無いので例外が発生