# Webアプリケーション
# http.serverモジュール HTPPサーバーの機能を提供する
# コマンドラインへ　python -m http.server --cgi

# Ｗebフレームワークを使用する
# Bottleフレームワーク
pip install bottle

import bottle

html = '''
<!DOCTYPE html>
<html lang="ja">
    <head>
        <meta charset="UTF-8">
        <title>Bottle</title>
    </head>
    <body>
        {}
    </body>
</html>    
'''
@bottle.route("/hello") # /helloにアクセスするとHello!
def helo():
    return html.format("Hello!")

@bottle.route("/bye")
def bye():
    return html.format("Bye!") # /byeにアクセスするとBye!
bottle.run(host="localhost", port=8000)

