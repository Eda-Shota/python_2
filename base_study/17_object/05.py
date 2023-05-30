# オブジェクトを支える属性の仕組み

class A:
    pass

a = A()
setattr(a, "x", 123) #　オブジェクトに属性を追加し、値を設定する
print(getattr(a, "x")) # 属性の値を取得
print(hasattr(a, "x")) # 属性の存在を確認
delattr(a, "x") # 属性を削除
print(dir(a)) # オブジェクトとクラスが持つ属性名の一覧を取得
print(vars(a)) # オブジェクトとクラスが持つ属性名と値の一覧を取得


class B:
    __slots__ = ["x", "y"] # スロット機能を使用する事で属性の追加の使用を制限し、メモリの消費量を抑制、処理の高速化が可能

b = B()
setattr(b, "x", 123)
setattr(b, "y", 456)