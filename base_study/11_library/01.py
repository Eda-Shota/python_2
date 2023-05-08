# プログラムにライブラリをインポートする

# プログラムからライブラリを利用するには、インポートが必要

# モジュール
# Pythonにおいては、プログラムファイル（.pyファイル）がモジュールとなる。

# パッケージ
# モジュールを詰め合わせたもの
# 大規模なライブラリでは、パッケージの中に細分化されたサブパッケージがある場合もある。

# import文
# ライブラリを取り込む
import random # import モジュール名
random.randint(1, 6) # モジュール名.変数名

import random as r # import モジュール名 as 別名
r.randint(1, 6) # 別名で呼び出せる

# from節
# from節を付けたimport文を使うと、モジュール名無しで機能を使える。
from random import randint # from モジュール名 import 機能名
randint(1, 6)

from random import randint as ri # from モジュール名 import 機能名 as 別名
ri(1, 6)

from urllib import parse # from パッケージ名 import モジュール名
print(parse.urlparse("https://www.python.org/"))

from urllib.parse import urlparse # from パッケージ名.モジュール名 import 機能名
print(urlparse("https://www.python.org/"))