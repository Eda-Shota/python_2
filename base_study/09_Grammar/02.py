# 内包表記
# データ構造を作成するときに役立つ。

# 内包表記を使わなかった場合(2乗の式)
a = []
for x in range(10):
    a.append(x*x)
print(a)
# 内包表記を使った例(リスト)
print([x*x for x in range(10)]) # [式 for 変数 in イテラブル]
# このように内包表記を使用すると、プログラムを短くまとめられる

# また他のデータ構造においても使用可能
# 集合も枠の種類を変えるだけで実現できる。
print({x*x for x in range(10)}) # {式 for 変数 in イテラブル]}

# 辞書の場合も同様だが、キーと値がある為、キーと値を生成する2個の式を:で区切る
print({x*x: x for x in range(10)}) # {キーの式: 値の式 for 変数 in イテラブル]}

# 内包表記で多重ループを表現
# 内包表記を使わなかった場合 (for文の中でさらにfor文による繰り返しが生じる九九の式)
a = []
for x in range(1, 10):
    for y in range(1, 10):
        a.append(x*y)
print(a)

# 内包表記を使った九九
print([x*y for x in range(1, 10) for y in range(1, 10)]) # [式 for 変数A in イテラブルA for 変数B in イテラブルB]

# 応用、九九を一段ずつ内側のリストに入れた外側のリストを作成。
print([[x*y for x in range(1, 10)] for y in range(1, 10)]) 

# 内包表記とifを組み合わせる
print([x for x in range(20) if x%2 and x%3]) # [式A for 変数 in イテラブル if 式B]
# 2の倍数でも3の倍数でもない数字を格納したリストを表示する。

# 内包表記と条件式を組み合わせる
# 内包表記を使わないFizzBuzz文
a = []
for x in range(1, 16):
    if x%15 == 0:
        a.append("Fizz Buzz")
    elif x%5 == 0:
        a.append("Buzz")
    elif x%3 == 0:
        a.append("Fizz")
    else:
        a.append(x)
print(a)
# 内包表記を使った場合
print(["Fizz Buzz" if x%15 == 00 else "Buzz" if x%5 == 0 else "Fizz" if x%3 == 0 else x for x in range(1, 16)])