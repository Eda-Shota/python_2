# if文
# if 式 :　の下に、インデントを空けて書くことで、条件分岐でコードを実行できる
number = "123456"
if number == "123456":
    print("1st Prize:Money")


number = input("number") # キーボードからの入力を取得するinput関数
if number == "123456":
    print("1st Prize:Money")
elif number[-4:] == "7890": # pythonではelif節　後ろから数えて四番目から一番後ろまでの数字。
    print("2nd Prize:Gift Box")
elif number[-2:] == "05": # pythonではelif節
    print("3rd Prize:Stamp Sheet")
else: # else節
    print("Lose")

# 条件式
number = input("Number:")
print("1st Prize:Money" if number == "123456" else "Lose")
# このように条件式を使うと短くまとめられる
# 先ほどelif節を用いて書いたコードは、このようにelseを入れる事で実現できる
number = input("Number:")
print("1st Prize:Money" if number == "123456" else
      "2nd Prize:Gift Box" if number[-4:] == "7890" else
      "3rd Prize:Stamp Sheet" if number[-2:] == "05" else "Lose")
# 可読性によってif文と条件式を使い分ける
