# str(ABC)　と　"ABC"　が同じ結果になる
# list(1, 2)　と　[1, 2]　が同じ結果になる
# これらのように簡単な記法が存在する

# クラスを定義
class Food: # クラスを定義
    pass

x = Food() # クラスを使ってオブジェクトを生成
x.name = "milk" # 生成されたオブジェクトのデータ属性nameへ代入
x.price = 150 # 生成されたオブジェクトのデータ属性priceへ代入
print(x.name, x.price)

y = Food() #　同じクラスを使って別のオブジェクトを生成
y.name = "egg"
y.price = 200
print(y.name, y.price)

# __init__メソッド
# イニシャライズの略で、データ属性を初期化するメソッド
# このメソッドはオブジェクトを生成するときに自動的に呼び出される
class Food: # クラスを定義
    def __init__(self, name ,price):
        self.name = name
        self.price = price

x = Food("milk", 150)
print(x.name, x.price)

y = Food("egg", 200)
print(y.name, y.price)
# 確実に初期化し、新しいオブジェクトを作る事が出来る

# メソッド
# クラスの内側では独自のメソッドを定義する事ができる、
# 処理の対象となるオブジェクトを指定して呼び出すメソッドはインスタンスメソッド
# クラスを指定して呼び出すメソッドは静的メソッドやクラスメソッドと呼ばれる。
# 定義したメソッドを呼び出すには、オブジェクト.メソッド名として呼び出す
class Food:
    def __init__(self, name ,price):
        self.name = name
        self.price = price

    def show(self): # showメソッドを定義
        print(self.name, self.price)

x = Food("milk", 150)
x.show() # showメソッドをXオブジェクトを対象に呼び出し

y = Food("egg", 200)
y.show() # showメソッドをyオブジェクトを対象に呼び出し

# Pythonのオブジェクトは全て、他の言語でいう所のpublicとなっている。
class Food:
    def __init__(self, name ,price):
        self.name = name
        self.price = price

    def show(self):
        print(self.name, self.price)

x = Food("milk", 150)
x.price //= 2 # xオブジェクトのpriceを二分の一
x.show()
#　なのでこのようにクラスの外部から変更を加える事が可能
# これを避ける場合は、属性名の頭に_をつけるのが慣習。(機能ではなく、_をつける事で変更しないでほしいという意思表示になる)
class Food:
    def __init__(self, name ,price):
        self._name = name
        self._price = price

    def show(self):
        print(self._name, self._price)

x = Food("milk", 150)
x.price //= 2 # うっかり変更しようとしても通常の記法であればエラーが生じるので気づく
x.show()

# __を頭文字に付ける事で、機能として外部からの変更を防ぐことができる(マングリング)
class Food:
    def __init__(self, name ,price):
        self.__name = name
        self.__price = price

    def show(self):
        print(self.__name, self.__price)

x = Food("milk", 150)
x.__price //= 2 # これでもエラーが生じるため、機能的に防ぐことが出来る。
x.show()
# ただし、._Food__priceのように属性指定をすれば使えてしまうので、絶対に防げるわけではなく。
# あくまで変更を防止する為の機能

class Food:
    count = 0

    def __init__(self, name ,price):
        self.name = name
        self.price = price
        Food.count += 1 # countを+1する。初期化の対象になっていない為、数値が初期化されない。

    def show(self):
        print(Food.count, self.name, self.price)

x = Food("milk", 150)
x.show()

y = Food("egg", 200)
y.show()