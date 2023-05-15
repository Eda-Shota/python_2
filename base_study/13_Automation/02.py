# システム管理の仕事を自動化する

# ファイルの追加や削除を監視する
# ファイル一覧を取得するglobモジュールと、時間待ちを行うtimeモジュールで
# カレントディクトリに対してファイルの追加や削除が行われた時に、その内容を表示するプログラムの例
import glob
import time
old = set(glob.glob("*")) # ファイル一覧を取得して、old変数に格納
while True: # 無限ループで実行
    time.sleeo(3) # 3秒の時間待ち。実際に活用するのであればもっと長くて良い
    new = set(glob.glob("*")) # ここを実行時のファイル一覧を取得    
    if added := new-old: # 新旧の差分から追加されたファイルを特定し、格納
        print("Added :", " ".join(added)) # 追加ファイルを表示
    if removed := old-new: # 旧新の差分から削除されたファイルを特定し、格納
        print("Eemoved :", " ".join(removed)) # 追加ファイルを表示
    old = new # 現在の状態にold変数を更新

# CPUやメモリの使用率を監視する(psutilライブラリ)
# psutilライブラリを使ってシステムの使用状況や、実行中のプロセスに関する情報を取得する
pip install psutil
# CPUの使用率を取得
print(f"CPU : {psutil.cpu_percent(interval=11):5} %") # psutil.cpu_percent(interval=秒数) 指定した時間内の使用率を取得
# メモリの使用率を取得
print(f"Memory : {psutil.virtual_memory().percent:5} %") # psutil.virtual_memory().percent メモリの使用率を取得
# psutil.virtual_memory().totalでメモリの全容量。psutil.virtual_memory().availableで使用可能容量を取得
# ディスクの使用率を取得
print(f"Disk : {psutil.disk_usage("/").percent:5} %") # {psutil.disk_usage(パス).percent ディスクの使用率を取得
# {psutil.disk_usage(パス).totalで全容量、{psutil.disk_usage(パス).usedで使用容量、{psutil.disk_usage(パス).freeで空き容量を取得

# 指定した条件で管理者にメールを送信する
# メールを作成するには、email.mime.textモジュールのMIMETextクラスを使用
# メールを送信するには、amtplibモジュールのSMTPクラスを使用
# メールを送る例
import smtplib
from email.mime.text import MIMEText

SERVER = "SMTPサーバ" # 実際の使用時は使用するサーバーを記入。以下も同様。変数に格納。
FROM = "送信元メールアドレス"
TO = "sousinnsakime-ruadoresu"
PASS = "パスワード"

mail = MIMEText("The disc is full") # メールの作成
mail["subject"] = "System Report" # 件名
mail["From"] = FROM # 送信元
mail["To"] = TO # 送信先

with amtplib.SMTP(SERVER, 587) as smtp: # SMTPオブジェクトをsmtp変数に格納
    smtp.ehlo() # EHLOコマンド クライアント名をサーバに伝える
    try: # TLSの接続を試みる
        smtp.starttls() # TLSを使ってサーバに接続する
        smtp.ehlo() # EHLOコマンド
    except smtplib.SMTPNotSupportedError: # TLSの接続に失敗した場合
        pass # そのまま続行
    smtp.login(FROM, PASS) # ログイン名とパスワードを使ってサーバにログインする
    smtp.sendmail(FROM, TO, mail.aas_string()) # 送信元、送信先、内容を指定してメールを送信する

# システムの状態を報告するメール
import psutil
import smtplib
from email.mime.text import MIMEText

SERVER = "SMTPサーバ"
FROM = "送信元メールアドレス"
TO = "sousinnsakime-ruadoresu"
PASS = "パスワード"
message = f"""
CPU : {psutil.cpu_percent(interval=11):5} %
Memory : {psutil.virtual_memory().percent:5} %
Disk : {psutil.disk_usage("/").percent:5} %

"""

mail = MIMEText(message)
mail["subject"] = "System Report"
mail["From"] = FROM
mail["To"] = TO

with amtplib.SMTP(SERVER, 587) as smtp:
    smtp.ehlo()
    try:
        smtp.starttls()
        smtp.ehlo()
    except smtplib.SMTPNotSupportedError:
        pass
    smtp.login(FROM, PASS)
    smtp.sendmail(FROM, TO, mail.aas_string())