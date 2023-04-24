# ジェネレータ
# あらかじめ複数の値を格納しておくのではなく、値を要求される度に生成する。
# それによってメモリの消費を抑えたり、無制限に値を生成する事が出来る
# ジェネレータを作成する方法には、ジェネレータ式とジェネレータ関数がある。

# ジェネレータ式は内包表記と同じ要領で作られる、
print((x*x for x in range(10))) # (式 for 変数　in イテラブル)
# ジェネレータ式は単独で実行するとジェネレータオブジェクトを返す

# 実際に使用する際には、内包表記と同じように使用できる
for y in (x*x for x in range(10)):
    print(y, end=" ")

# ジェネレータ関数を使うと、関数の定義と似た記法でジェネレータを作る事が出来る。
# ジェネレータ域では書きにくい複雑な処理を、ジェネレータ関数で表現できる。
def g():
    for x in range(10):
        yield x*x

for y in g():
    print(y, end" ")
# やっていることはジェネレータ式と同じで、冗長になる。
# 他の例
def my_range(strat, stop): # startを開始地とする変数ｘがstopの値よりも小さい間だけ繰り返す
    x = strat
    while x < stop:
        yield x
        x += 1

for y in my_range(100, 110):
    print(y, end=" ")

# yield from文
# yield文の代わりに、指定したジェネレータに値を返させるために使う
def my_range(strat, stop):
    x = strat
    while x < stop:
        yield x
        x += 1

def my_range2(start, stop, count):
    for i in range(count):
        yield from my_range(start, stop) # my_rangeのジェネレータを使用する

for y in my_range2(1, 10, 3):
    print(y, end=" ")