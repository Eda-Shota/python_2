print(1+2*3)
print(1+2*3, "なな")
# for文は繰り返し処理。以下は一文字ずつ出力する
for c in "python":
    print(c)
print ("プログラミング")

for c in "python":
    print(c, end="=>")
# lenは要素の数量を数える
print(len("python")+len("プログラミング"))
# インデントでまとめられた処理を3回繰り返す
for i in range(3):
    print("start")
    print("stop")
# 以下の形だとstartのみを三回繰り返す。インデントの深さを合わせる事が重要
for i in range(3):
    print("start")
print("stop")
