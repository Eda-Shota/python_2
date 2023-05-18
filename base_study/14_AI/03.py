# データを可視化する
# Matplotlib
# NumPyの配列やPandasのデータフレームなどから、色々な種類の図を作成する事が出来ます

# ヒストグタムを表示
pip install matoplotlib
import pandas
from mtplotlib import pyplot

score = pandas.read_csv("score2.csv", encoding="utf_8")
pyplot.igure("Math") # pyplot.figure(タイトル, figsize=(横,縦)) 図を作成(figure関数)
pyplot.xlabel("Score") # pyplot.xlabel(横軸名) 横軸名を指定
pyplot.ylabel("Count") # pyplot.ylabel(縦軸名) 縦軸名を指定
pyplot.hist(score["Math"]) # pyplot.hist(データフレーム) ヒストグラムを描写
pyplot.savefig("histl.png") # pyplot.savefig(ファイル名) 図をファイルに保存
pyplot.show() # pyplot.show() 図を画面に表示

score.hist()
pyplot.saving("hist2.png")
pyplot.show()

# 散布図を表示してみる

score.plot.scatter("English", "Japanese", s=100, c="white", edgecolor="black", figsize=(6, 6)) # score.plot.scatter(横軸, 縦軸)　散布図の作成
pyplot.savefig("scatter1.png")
pyplot.show()