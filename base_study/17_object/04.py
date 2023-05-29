# 静的メソッドとクラスメソッド
# 処理の対象となるオブジェクトを指定せず呼び出す為のメソッド

class Color:
    def __init__(self, r, g, b): # 文字列の初期化
        self.r, self.g, self.b = r, g, b

    def __str__(self): # 文字列の作成
        return f"({self.r}, {self.g}, {self.b})"
    
    @staticmethod
    def cyan():
        return Color(0, 255, 255)
    
    @staticmethod
    def aqua(): # aquaを性的メソッドとして定義
        return Color.cyan() # Colorクラスを呼び出し
    
print(Color.aqua())