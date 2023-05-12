# よく使う形式のファイルを読み書きする

# CSVファイルの出力
import csv # 標準ライブラリのcsvモジュールをインポート
catalog = [("hat", 2000), ("shirt", 1000), ("socks", 500)]
with open("catalog.csv", "w", encoding="utf-8", newline="") as file: # キーワード引数newlineに空文字を指定し、空行が余分に出力されることを防ぐ
    csv.write(file).writerows(catalog) # writeオブジェクトを作成した後に、writerowsメソッドを呼び出し、複数の行をまとめて書き込む
# 1行を書き込むwriterowメソッドもある。
# writerowメソッドは変数に代入しておいて再利用すると便利。
file2 = csv.write(catalog.csv)
file.writelow(catalog)

# csvファイルの入力
important csv
with open("catalog.csv", encoding="utf-8") as file: # 第二引数を略しているので"r"
    for row in csv.reader(file): # csvの各行を入力
        print(row) # 各行を表示
# csvファイルの内容をリストに格納する
import csv
with open("catalog.csv", encoding="utf-8") as file:
    print([tuple(x) for x in csv.reader(file)]) # タプルのリストを作成

# JSONファイルの出力
import json # jsonモジュールをインポート
catalog = [{"name": "hat", "price": 2000},{"name": "shirt", "price": 1000},]{"name": "socks", "price": 500}
with open("catalog.json", "w", encoding="utf-8") as file:
    json.dump(catalog, file, indent=4) # dump関数で開いたファイルにイテラブルの内容を書き込む。indentを指定するとインデントや改行が入るため人間が読みやすくなる。

# JSONファイルの入力
import json
with open("catalog.json", encoding="utf-8") as file:
    print(json.load(file)) # load関数で読み込む

# 画像ファイルの出力(Pillow)
# Pillowライブラリは非標準のライブラリであるため、インストールが必要
pip install pillow

from PIL import Image # PIL.Imageモジュールのインポート
image = Image.new("RGB", (640, 480), (255, 255, 0)) # イメージ = Image.new(モード, (幅, 高さ), 背景色)
image.save("yellow.png") # saveメソッドで保存

# グラデーション画像を作ってみる(putpixelメソッド)
from PIL import Image
W, H = 640, 480 # 画像サイズ
image = Image.new("RGB", (W,H), (0, 0, 0)) # 画像を作成
for x in range(W): # 横の大きさ分繰り返す
    for y in rnge(H): # 縦の大きさ分繰り返す
        image.putpixel((x, y), (x*255//W, y*255//H, ((W+H)-(x+y))*255//(W+H))) # イメージ.putpixel((X座標, Y座標), (R成分, G成分, B成分))
image.save("gradation.png")

# 画像ファイルの入力(Pillowライブラリ)
from PIL import Image
image = Image.open("gradation.png") # open関数で画像の読み込み
print(image.format, image.width, image.height) # フォーマット、幅、高さの情報を表示

# 拡張子を変えて保存
from PIL import Image
image = Image.open("gradation.png") 
image.save("gradation.jpg")