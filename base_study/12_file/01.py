# 基本はテキストファイルの読み書き

# テキストファイルの出力
# with文とopen関数
# open関数はファイルを開く組み込み関数、with文は内側の文を実行し終えると開いてきたファイルを自動的に閉じる
# 第二関数の"w"は書き込み、指定したファイルが無ければ新規作成し、ファイルがあれば上書きする。
# 他にも"a"追加書き込み、"r"は読み込み
with open("message.txt", "w", encoding="utf-8") as file: # with open(ファイル名, "w", encoding=文字エンコーディング) as 変数:
    file.write("Hello\n") # \nは改行
    file.write("Python\n")
    file.write("Programming\n")

# テキストファイルの入力
with open("message.txt", encoding="utf-8") as file: #　題に関数を略すことで "r"読み込みとなる。
    print(file.read()) # ファイルオブジェクト.read()　ファイルのテキストを全て読み込んで一個の文字列にする
# 一つずつ読み込む場合
with open("message.txt", encoding="utf-8") as file: # for 変数 in ファイルオブジェクト:
    for count, text in enumerate(file, 1):
        print(count, text, end="")