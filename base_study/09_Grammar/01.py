# 例外処理、エラーはどんな簡単なプログラムにも起こりうる。
# 例外処理を回避しようとすると、if文を多用したりして煩雑になり、処理の流れも分かりにくくなってしまう。
# Pythonにはtry節とexcept節が存在する。
# try節の中でエラーが発生した場合、処理を中断しexcept節を確認。指定したエラーと一致した場合は、その中のコードを実行する。
while True:
    try: # 例外が起きなければ滞りなく実行するコード
        price = int(input("price: "))
        count = int(input("count: "))
        print("price//count =", price//count)
    except ValueError: # 適切でない値が代入されている際のエラー。
        print("Input an integer.")
    except ZeroDivisionError: # 0で割り算等が行われた場合に発生するエラー
        print("The count must be != 0.")
    print("-"*25)
# このように正常な処理とエラー処理がはっきりと分かれて書かれるので、処理の流れが分かりやすい

# またexcept節は処理をまとめる事もできる。
while True:
    try:
        price = int(input("price: "))
        count = int(input("count: "))
        print("price//count =", price//count)
    except (ValueError, ZeroDivisionError): # 二つのエラーだった場合の処理をまとめている
        print("Error.")
    print("-"*25)
# except節 に何も記述しなければあらゆるエラーに対する例外処理となるが、
# Ctrl+cで終了もできなくなる。(キーボード割込みと言うエラーであるため)
# なのでExceptionという例外を指定すると良い
while True:
    try:
        price = int(input("price: "))
        count = int(input("count: "))
        print("price//count =", price//count)
    except Exception: # 大部分の例外の基底クラスであるため、ほぼすべての例外を処理できる。
        print("Error.")
    print("-"*25)
# さらに例外が発生した場合は、例外クラスのオブジェクトが発生しているため
# except節で受け取る事で例外に関する情報を受け取れる。
while True:
    try:
        price = int(input("price: "))
        count = int(input("count: "))
        print("price//count =", price//count)
    except Exception as e: # 変数eで例外オブジェクトを受け取る。
        print(e) # 受け取った例外オブジェクトを表示する
    print("-"*25)
#　各種エラーの内容を表示できる。

# ちなみにexcept節の中にpass文を書くと例外が発生した時に何も表示できなくできますが
# エラーのもみ消し状態になるため、危険

# finally節
# 例外が起きても起きなくても、最後に実行する処理。
while True:
    try:
        price = int(input("price: "))
        count = int(input("count: "))
        print("price//count =", price//count)
    except Exception as e:
        print(e)
    finally: # 例外の処理をしたとしても、枠だけは表示される
        print("-"*25)

# 例外が起きなかった場合にのみ実行したい場合はelse節
# exceptよりも後、finallyよりも前に書く
while True:
    try:
        price = int(input("price: "))
        count = int(input("count: "))
        print("price//count =", price//count)
    except Exception as e:
        print(e)
    else: # 例外が発生しなかった場合に処理を行う。
        print("Thank you.")
    finally: 
        print("-"*25)

# raise文を使う事で意図的に例外を起こす事もできる。
while True:
    try:
        price = int(input("price: "))
        if price < 0: # priceが負の値であった場合
            raise Exception("The price must be >= 0.") # raise文でExceptionを発生させ、例外の内容は()内
        count = int(input("count: "))
        print("price//count =", price//count)
    except ValueError: 
        print("Input an integer.")
    except ZeroDivisionError: 
        print("The count must be != 0.")
    except Exception as e: # Exceptionクラスは基底クラスなので、他の例外より下に書く。でないと、全てこれで処理されてしまう。
        print(e)
    else: # 例外が発生しなかった場合に処理を行う。
        print("Thank you.")
    finally: 
        print("-"*25)