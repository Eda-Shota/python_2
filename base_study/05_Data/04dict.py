# 辞書
# ミュータブルなので要素の追加や削除が出来る。
# 同じキーを重複して格納できない（値は重複しても良い）
# イミュータブルなキーの未格納できる（値はミュータブルでも良い）
# キーを取り出すときの順序は、キーを格納した時の順序に準ずる
lang = {"ja": "Japanese", "en": "English", "fr": "French"}
lang
dict[("ja": "Japanese"), ("en": "English"), ("fr": "French")] # dict関数を使用してイテラブルから辞書を作成
dict("ja": "Japanese", "en": "English", "fr": "French") # dict関数とキーワード引数で辞書御作成
# キーを重複して登録させることが出来ず、重複したキーがある場合、後の要素で上書きされる
lang["en"] # 値を習得できる。含まれていないキーを指定した場合、キーエラーが発生する
lang.get("en") #　値を取得できる。含まれていないキーを指定した場合もエラーが生じない。
lang.get("de", "German") # デフォルト値を設定した場合、含まれていないキーが指定されると、デフォルト値を返す。

# 要素の追加
lang["de"] = "German"
# 要素の変更
lang["de"] = "Deutsch"
# 要素の削除
del lang["de"] # del文
lang.pop("fr", "French") # popメソッド、デフォルト値を設定すれば、キーがない場合デフォルト値を返す
lang.clear # 全ての要素を削除 
# len関数, in, not inも使用可能
len(lang)
"fr" in lang
"de" not in lang
# キーの一覧を取得
lang.keys() # keysメソッド
# 値の一覧を取得
lang.values() # valuesメソッド
# キーと値の組の一覧を取得
lang.items() # itemsメソッド
# listを用いて、リスト化する事も可能
# 辞書自体もイテラブルであり、そのままリスト化すると、keysメソッドと同じ結果が得られる
list(lang)