# 簡単なライブラリを使ってみる

# randomモジュール
import random

## random関数
random.random() # random()

## choice関数
flavor = ["vanilla", "chocolate", "strawberry"]
random.choice(flavor) # choice(シーケンス)

## shuffle関数
random.shuffle(flavor) # shuffle(シーケンス)
flavor


# timeモジュール
import time

## time関数
time.time() # time()

## gettime関数
time.getime() # getime()

## localtime関数
time.localtime() # localtime()

## sleep関数
time.sleep(3) # sleep(秒数)
