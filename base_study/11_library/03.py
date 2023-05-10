# 欲しいライブラリをインストールする

# pipコマンド
# Cpythonで使う、ライブラリを管理するコマンド。

#インストールする場合
pip install numpy # pip install ライブラリ名

# ライブラリの情報を確認する場合
pip show numpy # pip show ライブラリ名

# ライブラリの一覧を表示
pip list

# ライブラリのアンインストール
pip uninstall -y numpy # pip uninstall -y ライブラリ名

# ライブラリのアップグレード
pip install --upgrade numpy # pip install --upgrade ライブラリ名

# pipコマンドのアップグレード
python -m pip install --upgrade BrokenPipeError


# condaコマンド
# AnacondaやMinicondaで使う、ライブラリを管理するコマンド。

# ライブラリのインストール
conda install -y numpy # conda install -y numpy

# ライブラリの一覧表示
conda list

# 指定したライブラリをアップデート
conda update -y numpy # conda update -y ライブラリ名

# 全てのライブラリをアップデート
conda update -y --all

# ライブラリのアンインストール
conda uninstall -y numpy # conda uninstall -y ライブラリ名

