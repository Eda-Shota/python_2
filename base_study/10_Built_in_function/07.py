# オブジェクトやクラスについて調べる関数

# id関数 オブジェクトが配置されているメモリのアドレスを返す
# hash関数 オブジェクトのハッシュ値を返す
# super関数 派生クラスから基底クラスのメソッドを呼び出すときに使う

# type関数
# オブジェクトの型を現すtypeオブジェクトを返す
type(123)
type("python")
type([4, 5, 6])

# isinstanece関数
# 指定したオブジェクトが指定したクラスのインスタンスであればTrueを返す
isinstance(123, int)
isinstance("python", str)
isinstance([4, 5, 6], list)

# issubclass関数
# 指定したクラスAがクラスBと同一である場合にTrueを返す
class A:
    pass

class B(A):
    pass

class C(A):
    pass

print(issubclass(C, A))
print(issubclass(C, B))