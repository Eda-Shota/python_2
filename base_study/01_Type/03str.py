# str型　文字列型
# 縦に並べただけでは連結されるだけ
print(
"前半部分のテキスト"
"後半部分のテキスト"
)
# 複数行にわたるテキストにしたい場合
print("""\
前半部分のテキスト
後半部分のテキスト\
""")
# \や￥を使用している文字列を表示したい場合は「r」raw文字列を書く
print(r"￥100/25")