#必要なデータの抽出
# Pandasライブラリ
# データの読み込み、指定したデータの取得、統計量の計算を簡単なプログラムで実現できる。
# 主要な機能はDataFrameと呼ばれるオブジェクト。CSVファイルから読み込んだ表をデータフレームに格納し、特定の要素を取得したり、各種の演算が行える

pip install pandas
import pandas
score = pandas.read_csv("score2.csv", encoding="utf_8") # データフレーム = pandas.read_csv(ファイル名, encoding=文字エンコーディング)　CSVファイルの読み込み
score
score.head(3) # データフレーム.head(行数) 最初~指定した行数分を取得
score.tail(3) # データフレーム.tail(行数) 最後~指定した行数分を取得

# データフレームの列や行や要素を取得する
score["Japanese"] # データフレーム[列名] 指定した列を取得し、列の情報も得られる
score[["Japanese", "English"]] # データフレーム[[列名, …]] 複数の列をまとめて取得
score[2:4:2] # データフレーム[開始行番号:終了行番号:ステップ] 指定した行を指定したステップで取得
score[["Japanese", "English"]] [2:4] # データフレーム[列のインデックス][行のスライス] 行と列を指定して要素を取得

# 条件に基づいてデータフレームの要素を取得する
score[score["Japanese"] >= 95] # データフレーム[式]
score.query("Japanese >= 95") # 条件に合う要素だけを取得(queryメソッド)
# allやanyメソッドを使う方法も有効
score[(score == 100).any(1)]

# 計算の結果をデータフレームに出力する
score["Total"] = score["English"]+score["Math"]+score["Japanese"] # データフレーム[列名] = 値
del score["Total"] # del データフレーム[列名]
score["Total"] = score.sum(1) # データフレーム.sum(軸番号) 指定した軸について合計を求める(sumメソッド)
score.to_csv("score.csv") # CSVファイルに保存