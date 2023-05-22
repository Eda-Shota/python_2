# スクレイピングを定期的に実行
# scheduleライブラリ 予め指定下スケジュールに基づいて指定した処理を呼び出してくれる。
pip install schedule

import schedule
import time
import scraping

schedule.every().day.at("12:00").do(scraping.job) # 毎日12時にscrapingファイルのjob関数を実行

while True: # 無限ループ
    schedule.run_pending() # スケジュールを実行
    time.sleep(1) # 1秒待ち