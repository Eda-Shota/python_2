# 代入式
# 式の中で変数に値を代入する事が出来る、
# := 式 こんな形なのでセイウチ演算子とも呼ばれる。
# 代入式を使うと、プログラムが短くなるが、分かりづらくもなる。
# 使わない場合
while True: # qが入力されると繰り返しが終了する式
    x = input()
    if x == "q":
        break
    print(x)

# 代入式を使用する場合
while (x := input()) != "q":
    print(x)

# 別の例
t = 0
while True: # qが入力され鵜まで、入力された数値を合算して表示する
    x= input("price: ")
    if x == "q":
        break
    t += int(x)
    print("total:", t)
# 代入式を使用する場合
t = 0
while (x := input("price: ")) != "q":
    print("total:", t := t+int(x))