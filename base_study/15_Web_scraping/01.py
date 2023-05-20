# Webページを取得する方法
# urllib(標準パッケージ)を使って、取得する方法
from urllib.request import urlopen
with urlopen("https://higpen.jellybean.jp/") as file: # Web上のファイルを開く
    for line in file: # １行ずつ読み込む
        print(str(line, encoding="utf-8"), end="") # バイト列を文字列に変換して表示

with urlopen("https://higpen.jellybean.jp/") as web_file: # Web上のファイルを開く
    with open("download.html", "wb") as local_file: # ファイルを開く
        local_file.write(web_file.read()) # ローカルファイルに保存

# Requestsライブラリを使って、取得する方法
# 標準ライブラリよりも簡潔なプログラムで扱える
pip install requests
import requests
r = requests.get("https://higpen.jellybean.jp/") # レスポンス = requests.get(URL)ファイルを取得
print(r.text) # レスポンス.text Web上のファイルの内容を取得

with open("download2.html", "wb") as file: # ローカルファイルを開く
    file.write(r.content) # 保存