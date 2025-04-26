# Flask というwebアプリの本体を作る為のクラスをインポートする。この行がないとFlaskアプリを起動できない。
from flask import Flask

# Flaskのアプリケーションを作成する関数を定義する。
# この関数はFlaskのアプリケーションを作成し、必要な設定やルーティングを行うために使用されます。
def create_app():
    #  Flaskクラスのインスタンス（アプリ本体）を作成しています。  
    # `__name__` を使うことで、Flaskがどこから実行されたかを理解し、静的ファイルやテンプレートの場所を把握できるようになります。
    app = Flask(__name__)

    # 同じappフォルダ内のroutes.pyを読み込んでいる
    # これにより、Flaskアプリケーションにルーティングの設定を追加することができます。
    # ルーティングとは、特定のURLに対してどの関数を呼び出すかを決定する仕組みです。
    from . import routes
    # routes.pyで定義されているBlueprint(機能の纏まり)をFlaskアプリに登録している。
    # これにより、routes.py内で定義されたルート(URLとの対応処理)やビュー関数がFlaskアプリに追加されます。
    app.register_blueprint(routes.bp)

    # 作成したアプリ本体を返す。  
    return app
