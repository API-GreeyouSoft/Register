import sqlite3

# データベースに接続
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# 新しいユーザーを登録
def register_user(username, password):
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()

# ユーザーのログインを確認
def login_user(username, password):
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    return user

# データベース接続を閉じる
conn.close()
