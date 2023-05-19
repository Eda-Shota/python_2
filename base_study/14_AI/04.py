# データに機械学習を適用する
# scikit-learnライブラリ
# データに対して、分類、怪奇、クラスタリング、次元削減といった、機械学習に関する色々な手法を適用する事が出来る。
pip install scikit-learn

import pandasfrom matplotlib import pyplot
from sklearn.cluster import KMeans # sklernパッケージの中のclusterモジュールにあるKMeansクラスをインポート

score = pandas.read_csv("score2.csv", encoding="utf_8")
model = KMeans(n_clusters=3).fit(score[["English", "Japanese"]]) # モデル = KMeans(n_clustera=クラスタ数).fit(データフレーム) クラスタリングのモデルを作成

score["Cluster"] = model.labels_ # Cluster列を追加し、見やすく
score.to_csv("score4.csv")
print(score)

# 散布図に
score.plot.scatter("English", "Japanese", s=100, c=score["Cluster"], edgecolor="black", figsize=(6, 6))
pyplot.savefig("scatter2.png")
pyplot.show()