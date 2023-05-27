# 特殊メソッド
# 前後に_が2個ずつ突いた、特殊な名前のメソッド

# __str__メソッド
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self): # プリント関数でオブジェクトを出力する
        return f"({self.x}, {self.y})"

print(Point(1, 2))


# 算術演算子の特殊メソッド
# 定義する事で算術演算子をオブジェクトに適用できるようになる

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self,other): # 加算の特殊メソッド
        return Point(self.x+other.x, self.y+other.y)
    
    def __mul__(self,other): # 乗算の特殊メソッド
        return Point(self.x*other, self.y*other)
    
print(Point(1, 2)*3)