# SQLを使ってデータベースを操作

# データベースを作成
import sqlite3
con = sqlite3.connect("shop.db") # データベースに接続
cur = con.cursor() # データベースに対する操作機能のカーソルオブジェクトを取得
cur.execute("DROP TABLE IF EXISTS account") # SQL文を実行　accountテーブルがあれば削除
cur.execute("CREATE TABLE account (user TEXT PRIMARY KEY, password TEXT)") # SQL文を実行 accountテーブルを作成、user列とpassword列を追加する
con.commit() # コミット
con.close() # 接続を閉じる

# データを登録
con = sqlite3.connect("shop.db")
cur = con.cursor()
account = [("suzuki", "abc123"), ("satou", "def456"), ("tanaka", "ghi789")] # 登録するリスト
cur.executemany("INSERT INTO account VALUES (?, ?)", account) # データを登録
con.commit()
con.close()

# データを取得して表示
con = sqlite3.connect("shop.db")
cur = con.cursor()
cur.execute("SELECT * FROM account") # accountテーブルから全ての行を取得
for user, password in cur: # 1行ずつ取り出す
    print(f"{user:10}{password}") # 結果を表示
con.close()

# 既存のデータを更新する
con = sqlite3.connect("shop.db")
cur = con.cursor()
user = "suzuki"
password = "cba321"
cur.execute("UPDATE account SET password=? WHERE user=?", (password, user)) # 指定したユーザーの列のパスワードを更新
con.commit()
con.close()

# ログイン機能の作成
import sys
if len(sys.argv) != 3: # コマンドラインの引数が３でなければ
    sys.exit(f"Usage: python {sys.argv[0]} user password") # 使い方を表示
con = sqlite3.connect("shop.db")
cur = con.cursor()
cur.execute("SELECT * FROM account WHERE user=? AND password=?", sys.argv[1:])
print("Welcome!" if list(cur) else "Failed.")
con.close()