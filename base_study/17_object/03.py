# デコレータ
# 関数やクラスに特別な機能を付加する。

# プロパティでデータ属性の取得や設定を制御する

class Item:
    def __init__(self, name, price)
        self.name = name
        self.__price = price

    @property # クラス外から呼び出された場合に、指定した値を返し。外部からの変更はできないようになっている。
    def name(self):
        return self.__name
    
    @property
    def name(self):
        return self.__price
    
    @price.setter # 外部からプロパティを設定できるようにしたが、負数が設定された場合に値が0になるようになっている。
    def price(self,value):
        self.__price = max(value, 0)
    
x = Item("burger", 100)
print(x.name, x.price)

x.price = 110
print(x.name, x.price)

x.price = -100
print(x.name, x.price)