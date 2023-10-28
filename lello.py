import sqlite3

# データベースに接続
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# ユーザーテーブルを作成
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  username TEXT NOT NULL,
                  password TEXT NOT NULL
                )'')

# データベースに変更を保存
conn.commit()

# データベース接続を閉じる
conn.close()
