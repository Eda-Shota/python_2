# ファイルに関連する色々な操作

# ファイル一覧の取得

import glob # globモジュールのインポート
for x in glob.glob("catalog.*"): # glob.glob(パス) globモジュールのglob関数

import glob
total = 0 # 合計を0で初期化
for x in glob.glob("catalog.*"): # ファイルの一覧を取得
    with open(x, encoding="utf-8") as file: # 各ファイルを開く
        s = file.read() # ファイルを読み込む
        n = s.count("\n")+1 if len(s) else 0 # 行数を計算
        print(f"{x:15}{n:5}") # 行数を表示
        total += n # 行数を合計に加算
print("-"*20) # 区切りを表示
print(f"{"Total":15}{total:5}") # 合計を表示

# ファイルのコピー、名前の変更、削除
import shutil
import os

shutil.copy("message.txt", "message2.txt") # shutil.copy(コピー元, コピー先)　ファイルのコピー
shutil.move("project/message.txt", "project2/message.txt") # shutil.move(移動元, 移動先)　ファイルの移動
os.rename("message2.txt", "message3.txt") # os.rename(古い名前, 新しい名前)　リネーム
os.remove("message3.txt") # os.remove(パス) 削除
os.mkdir("document") # os.mkdir(パス) ディレクトリの作成
os.rmdir("document") # os.rmdir(パス)　ディレクトリの削除
os.makedirs("project/programming/python") # os.makedirs(パス)　途中で必要なディレクトリもまとめて作成
os.removedirs("project/programming/python") # os.removedirs(パス)　最下層の実ではなく途中のディレクトリも削除

# コマンドライン引数の取得
>type message.txt # >コマンド 引数 …
# sysモジュール
import sys # コマンドライン引数を取得するために、sysモジュールをインポート
print(sys.argv) #sys.argv[インデックス] プログラム名を取得。インデックスは0がプログラム名、1以降が引数

import sys
print(sum(map(int, sys.argv[1:]))) # コマンドライン引数で与えられた整数の合計を表示