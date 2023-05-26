# ダックタイピング
# あるオブジェクトがいつ様なデータ属性やメソッドを備えていれば、どのクラスのオブジェクトであるかは問わない
def add(x, y):
    print(x, "+", y, "=", x+y)

add(1, 2)
add("Hello", "Python")
# どちらも表示できる。+演算子に対応してさえいればどのクラスでも同じ式で表示が可能。
# ダックタイピングを利用している言語であれば可能。採用していない場合は、決められたクラスのオブジェクトのみ受け入れる。


# 抽象クラス
# オブジェクトを作れないクラス。
# 基底クラスとして役立ち、抽象基底クラスと呼称する。
# その定義にabcモジュールを使用する。

from abc import *

class Command(ABC): # ABCクラスからCommandクラスを派生
    @abstractmethod
    def run(self, text): # 抽象メソッドのrunを定義
        pass

class Append(Command): # CommandクラスからAppendクラスを派生
    def __init__(self, text): # オブジェクトを初期化
        self.text = text # データ属性に代入

    def run(self, text): # コマンドを実行
        return text+self.text # テキストを追加
    
class Insert(Command): # Insertクラスの定義
    def __init__(self, index, text): # オブジェクトの初期化
        self.index = index # インデックスを保存
        self.text = text # テキストを保存

    def run(self, text): # コマンドの実行
        i = self.index # インデックスを取得
        return text[:1]+self.text+text[i:] # テキストを挿入
    
c = [Append("th"), Insert(0, "py"), Append("om")] # コマンドのリスト
s = "" # 空文字列
for x in c: # 繰り返し
    s = x.run(s) # コマンドを実行
print(s) # 結果を表示