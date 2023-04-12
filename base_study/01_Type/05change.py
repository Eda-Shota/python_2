# 型の変換
# int型への変換　整数化
int(1.2)
# 結果が環境によって異なる可能性がある為
# 標準ライブラリ「math」に含まれる関数の使用が推奨される
# ライブラリの読みこみは「import ライブラリ名」
import math
# 小数点以下を切り捨てる関数
math.floor(1.2)
# 小数点以下を切り上げる関数
math.ceil(1.2)
# 文字列をintに
int("123")
# 真偽も変換が可能
int(True)
int(False)

# floatへの変換
float(123)
float("123")
float(True)
float(False)

# strへの変換　文字列に変換する
str(123)
str(1.23)
str(True)
str(False)

# boolへの変換
bool(123)# True
bool(0)# False
bool("0")# True
bool(0.0)# False
bool("")# False
bool("False")# True
str(False)# False