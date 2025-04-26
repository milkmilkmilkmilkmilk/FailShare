from flask import Blueprint, render_template, request, redirect, url_for
# ここでBlueprintを作成している。mainはBlueprintの名。__name__はこのファイルの場所を教える為の値
bp = Blueprint('main', __name__)

# 
posts = [] # 投稿データを格納するリスト。実際のアプリケーションではデータベースを使用することが一般的です。

# 投稿一覧
@bp.route('/')
def index():
    return render_template('index.html')

# このルートは /create というURLにアクセスがあったときに実行されます。
# methods=['GET', 'POST'] によって、フォームの表示（GET）と送信（POST）の両方に対応できます。
@bp.route('/create', methods=['GET', 'POST'])

# create() という関数を定義します。投稿フォームの表示と、フォームからのデータ受け取りを両方扱います。
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        posts.append({'title':title, 'content': content})
        print('新しい投稿: {title} - {content}') # 投稿内容をサーバー側で確認するためにターミナルに表示します。デバッグ目的です。
        return redirect(url_for('main.index')) # 投稿が完了したら(/)にリダイレクトしている。url_for('main.index')でindex()関数のURLを自動で取得。
    return render_template('form.html')    

@bp.route('/posts')
def posts():
    dummy_posts = [
        {'title': 'タイトル壱', 'content': 'Hello World!'},
        {'title': 'タイトル弐', 'content': 'Flask is great!'},
        {'title': 'タイトル参', 'content': 'Python is awesome!'}
    ]
    # ダミーの投稿データを作成しています。実際のアプリケーションでは、データベースから取得することが一般的です。
    return render_template('posts.html', posts=dummy_posts)

