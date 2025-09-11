# Flask というwebアプリの本体を作る為のクラスをインポートする。この行がないとFlaskアプリを起動できない。
from flask import Flask
import os

# Flaskのアプリケーションを作成する関数を定義する。
# この関数はFlaskのアプリケーションを作成し、必要な設定やルーティングを行うために使用されます。
def create_app():
    #  Flaskクラスのインスタンス（アプリ本体）を作成しています。  
    # `__name__` を使うことで、Flaskがどこから実行されたかを理解し、静的ファイルやテンプレートの場所を把握できるようになります。
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object("config")

    # 同じappフォルダ内のroutes.pyを読み込んでいる
    # これにより、Flaskアプリケーションにルーティングの設定を追加することができます。
    # ルーティングとは、特定のURLに対してどの関数を呼び出すかを決定する仕組みです。
    from . import routes
    # routes.pyで定義されているBlueprint(機能の纏まり)をFlaskアプリに登録している。
    # これにより、routes.py内で定義されたルート(URLとの対応処理)やビュー関数がFlaskアプリに追加されます。
    app.register_blueprint(routes.bp)

    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    # Set UPLOAD_FOLDER to instance/uploads
    app.config['UPLOAD_FOLDER'] = os.path.join(app.instance_path, 'uploads')

    # Dynamically set the database URI
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path, "app.db")

    # Initialize extensions
    from .extensions import db, migrate
    db.init_app(app)
    # Ensure models are imported so Flask-Migrate can detect them
    from . import models  # noqa: F401
    migrate.init_app(app, db)

    # 作成したアプリ本体を返す。  
    return app
