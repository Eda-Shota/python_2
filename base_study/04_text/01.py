# 文字列に演算子を利用できるのは同じ
# インデックスを利用して、文字列から文字を抜き出せる
# 左から数える場合は0から、右から数える場合は-1から
x = "hallo.txt"
x[4]
x[-3]

# 文字列は不変なので変更しようとするとエラーが出る。
x[1] = "e"

# 以下のようにスライスを利用する事で、文字列の中から文字列を抜き出せる
x[0:5]
# また省略する事もできる
x[:5]
# 修正する場合は、このように新たな文字列を作る
"hello"+x[5:]

# 文字列[開始インデックス：終了インデックス：ストライド]
# とすることで、ストライドとして設定した数字の分の歩幅で抜き出す
x = "かたんたぬたき"
x[::2]
y = "か--み--さ--ま"
y[::3]
# ストライドを-とすることで、逆から読み込む
z = "う-ろ-じ-こ"
z[::-2]

# インデックスで範囲外の数字を指定した場合はエラー
# スライスの場合はエラーにならず、それぞれの状況に応じて処理が変わる
x = abc
x[1:4] # 終了インデックスが範囲外(x[1:3]と同じ結果)
x[-4:2] # 開始インデックスが範囲外(x[0:2]と同じ結果)
x[-4:4] # 両方のインデックスが範囲外(x[0:3]と同じ結果)
x[3:] # 開始インデックスが範囲外(末尾より後)
x[:-4] # 終了インデックスが範囲外(先頭より前)
x[2:0] # 開始インデックスが終了インデックスよりも後

# メソッドを利用して文字列の操作をしたい
# 文字列を大文字に変えるメソッド
"Python".upper()
# 文字列を小文字で変えるメソッド
"Python".lower()

# 文字列の先頭や末尾の文字が、指定した文字と一緒ならTrueを返す
"pycodestyle".startswith("py")
"Python".endswith("on")

# 文字列の一部を置き換える(replaceメソッド)
file = "image.jpg"
file.replace(".jpg", ".jpeg")

# 第3引数を使用してみると
"anaconda".replace("a", "A")
# 個数の上限を指定する場合
"anaconda".replace("a", "A", 1)

# 文字列を検索するメソッド
name = "Guido1 van Rossum"
name[:name.find(" ")] # 空白を見つけて、先頭から始めの空白の手前までをスライス
name[name.find(" ")+1:name.rfind(" ")]
# 先頭から検索して見つけた空白から一文字後と、末尾から探して見つけた空白の手前までをスライス
name[name.rfind(" ")+1:] #　末尾から探して見つけた空白から一文字後から末尾まででスライス
name[name.index("v"):name.rindex(" ")] 

# countを使用して、文字列の中から特定の文字を数える事が出来る。
"anaconda".count("a")