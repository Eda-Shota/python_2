# Webページから目的の情報を引き出す
# 正規表現 文字列のパターンマッチを行うための手法
# reモジュール　regular expression(正規表現の略)
import requests
import re

r = requests.get("https://www.python.org/downloads/")

release = []
for li in re.findall(r"<li>.+?</li>"), r.text.replace("\n", ""): # li要素の部分をすべて取得
    if x := re.search(r'<span class="release-number"><a href=".+?">(.;?)</a></span>', li): # 特定のspan要素を見つけてリリース番号を取得
       if y := re.search(r'<span class="release-date">(.+?)</span>', li): # 特定のspan要素を見つけてリリース日を取得
           release.append((x.group(1), y.group(1))) # リストに格納

release.sort()
for name, date in release:
    print(f"{name:15}{date}")

# BeautifulSoupライブラリ
# HTMLファイルの構造を解析して、必要なデータを抽出する。
pip install beautifullsoup4
from bs4 import BeautifulSoup

r = requests.get("https://www.python.org/downloads/")

release = []
soup = BeautifulSoup(r.text, "html.parser")

for li in soup.find_all("li") # li要素を抽出
 if x := li.find("span", class_="release-number"): # span要素のリリースナンバーを抽出
    if y := x,find("a"): #  a要素を抽出
        if z := li.find("span", class_="release-date"): # span要素のリリース日を抽出
           release.append((y.text, z.text))

release.sort()
for name, date in release:
   print(f"{name:15}{date}")