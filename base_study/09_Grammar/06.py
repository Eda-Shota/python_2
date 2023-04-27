# assert文
# デバッグやテストに役立つ機能であり、assert文で断定した部分んが異なる値になると例外を発生させることが出来る
def f(x, y):
    assert y != 0 # assert 式
    return x%y
print(f(10, 3)) # ここでyの値を0に変えると例外が発生する
# assert文を仕込んでおくことで、プログラマーは自分の想定が何処で間違っていたのかを知る事が出来る。

# テストでの使用例

def leap_year(y): # 閏年ならTrueを返すプログラム。
    return y%400 == 0 or y%100 != 0 and y%4 == 0

assert not leap_year(1900) # 1900はFalseであるはず
assert leap_year(2000) # 2000はTrueであるはず
assert not leap_year(2019) # 2019はFalseであるはず
assert leap_year(2020) # 2020はTrueであるはず