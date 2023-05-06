# プログラムの実行にかかわる関数
# eval関数
# 指定した文字列をPythonの式として評価し、式の値を返す。

while True:
    print("=", eval(input())) # eval(文字列)　入力された文字列をPythonの式として値を返す

# exac関数
# 指定した文字列をPythonプログラム式として実行。値は返さない。
# exac(コードオブジェクト)として、コードブジェクトを実行する事も可能。
while True:
    exec(input())

# compile関数
# 指定された文字列やファイルの内容をPythonのプログラムとしてコンパイルし、
# コードオブジェクトを返す
While True:
exec(compile(input(), "<string>", "exec"))

# globals関数
# グローバルな名前の一覧を、値と共に辞書で返す。
# lovals関数
# ローカルな名前の一覧を、値と共に辞書で返す。
def f():
    x = 123
    print("locals:" locals())

f()
y = 456
print("globals", globals())

# callable関数
# 指定したオブジェクトが呼び出し可能な場合にTrueを返す
callable(123)
callable("hello")
callable(len)
callable(list)

# breakpoint関数
# プログラムの実行を一時停止してデバッガに制御を移す。
x - 123
breakpoint()
y = 456
z = 789
breakpoint()
print(x, y, z)

# help関数
# 指定したオブジェクトの説明を表示する
help(abs)
def prime(n):
    """引数が素数ならばTrueを返す。"""
    return n > 1 and all((n%i for i in range(2, n)))

help(prime)