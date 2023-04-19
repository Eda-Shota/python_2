# 変数のスコープ（有効範囲）は、作成場所によって変わる。
# 関数の外側で作成した場合はグローバル変数。関数の外側でも内側でも使える
# 関数の内側で作成した変数はローカル変数、関数の内側でのみ使える
def f():
    print("f():", text)

def g():
    text = "Good Night" # ローカル変数。関数内のみで適用
    print("g():", text)

text = "Hello" # グローバル変数。関数より後にあっても良いが、呼び出すコードよりも前にならなければならない
f()
g()
print(text)

def f():
    global text # グローバル変数として呼び出される。
    text = "Good Bye"
    print("f():", text)

text = "Hello" 
f() # ここでグローバル変数がに代入されるので、
print(text) # ここでは関数内で代入された値が適用される。

def f():
    def g():
        nonlocal text # こうするとdef f内のローカル変数に代入される。
        text = "Good Night"
        print("g()", text)

    text = "Good Morning"
    g() # ここでローカル変数がよびだされ
    print("f()", text) # そのためここのテキストにはGoodNIghtが入る。

f()