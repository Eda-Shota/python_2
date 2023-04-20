# 派生と継承
# とある基底クラスから派生した派生クラスには、基底クラスの機能が継承されている。
# 派生クラス内に記述がなくとも、基底クラスのコードが適用される。
class Item: # 基底クラス。FoodやToyの共通項をここにまとめて、リーダブル化。
    def __init__(self, name ,price): # 商品名と値段は共通項
        self.name = name
        self.price = price

    def show(self): # 表示も同様
        print("name:", self.name)
        print("price:", self.price)

class Food(Item): # 派生クラス。Itemから派生している。
    def __init__(self, name ,price, use_by_date): # 基底クラスの同様のメソッドをオーバーライド
        super().__init__(name, price) # superで上書き前の基底クラスのメソッドを呼び出せる。
        self.use_by_date = use_by_date # クラス独自の項目を記述。

    def show(self): #基底クラスの同様のメソッドをオーバーライド。
        super().show()
        print("use-by date:", self.use_by_date)

    def eat(self):
        print("eating", self.name)

class Toy(Item):
    def __init__(self, name ,price, target_age):
        Item.__init__(self, name, price) # Itemクラスのメソッドを呼び出すという手もある
        self.target_age = target_age

    def show(self):
        Item.show(self) # Itemクラスのメソッドを呼び出すという手もある
        print("target age:", self.target_age)    

    def play(self):
        print("playing with", self.name)  

x = Food("chocolate", 100, 180)
x.show()

print()

y = Toy("figure", 350, 3)
y.show()
# super関数を使う方法と基底クラス名を使う方法があるが、
# 前者の方が、クラス名が変わっても修正の必要が無い。

# 派生クラスは多重継承が可能。
class Shokugan(Food, Toy): # 多重継承した派生クラス
    def __init__(self, name, price, use_by_date, target_age):
        self.name = name
        self.price = price
        self.use_by_date = use_by_date
        self.target_age = target_age

    def show(self): # 継承したメソッドを呼び出すだけなので、省略しても良いもの
        super().show()

x = Shokugan("chocolate+figure", 450, 180, 3)
x.show()
x.eat()
x.play()

# メソッドの呼び出し順は__mro__で確認できる
print(Shokugan.__mro__)
# 一番最後にあるobjectクラスは、Pythonにおける全てのクラスの基底クラス
# superを使ってメソッドを探す場合は、この順番の前の方から探す