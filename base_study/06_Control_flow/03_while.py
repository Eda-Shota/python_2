# whileは式の値がTrueである限り繰り返す。
catalog = []
while len(catalog) < 3: # カタログの要素の数が3より低い限り実行
    item = input("item: ") # item変数に直接入力
    catalog.append(item) # カタログのリストに入力した要素を追加
print("catalog:", catalog) # catarogのリストの要素を表示

# continue文
# whileやforの内部で使う。continue文を使うと、その後の処理を実行せずに、次の繰り返しへ移る
catalog = []
while len(catalog) < 3:
    item = input("item: ")
    if item in catalog: # 入力した値が既にリストに存在している場合
            print(item, "is on the catalog.") # そのアイテムは存在していると表示
            continue # 次の繰り返しへ移行
    catalog.append(item)
print("catalog:", catalog)

# break文
# こちらはその後の処理を中断し、繰り返し処理も中断する。
catalog = []
while len(catalog) < 3:
    item = input("item: ")
    if item in catalog:
            print(item, "is on the catalog.")
            break # くり替え処理ごと中断、リストの表示に移行
    catalog.append(item)
print("catalog:", catalog)

# else節
# break文で中断しない場合に限り、別の処理を実行する。
catalog = []
while len(catalog) < 3:
    item = input("item: ")
    if item in catalog:
            print(item, "is on the catalog.")
            break
    catalog.append(item)
else: # 繰り返し処理の条件式がFalseになった場合以下を実行。break文が実行された場合は表示されない
    print("catalog:", catalog)
# for文の場合は、全ての要素を処理し終えるとFalseになる。
# 無限ループはbreak文によって中断させる。
while True:
      word = input("word: ")
      if not word: # 空欄を入力した場合
            break # 処理を中断する
      print(len(set(word))) # 要素の数を出力
      print(set(word)) # 要素を出力