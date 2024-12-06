import streamlit as st
import sqlite3
import pandas as pd

#先ほど設定したDBの名前
db_name = 'datasets.db'

select_all_sql = 'select ' + '*' + ' from ' + 'tips'
with sqlite3.connect(db_name) as conn:
    df_from_sql = pd.read_sql(select_all_sql, conn)

#列名を取り出す
df_from_sql_columns = df_from_sql.columns

#####stゾーン開始

option = st.selectbox(
    'どの列がはいっているデータを抽出しますか？',
    (df_from_sql_columns)
)

num = st.text_input('数字を半角で入力してください :例 0.04')
#列と入力値両方が入力されるまで待つためのif文
if not option or not num:
  st.title("列と数字が入力されるまで待ちます")
else:
  st.title("選択されました")
  def sql1(columns, num2):
    sql = 'select ' + '*' + ' from ' + 'tips' + ' where ' + columns + ' > ' + num2
    return sql
  sql2 = sql1(option, num)
  with sqlite3.connect(db_name) as conn:
      df_from_sql2 = pd.read_sql(sql2, conn)
  st.dataframe(df_from_sql2)
#####stゾーン終了

"""import sqlite3
import streamlit as st
 
# SQLiteデータベースに接続
conn = sqlite3.connect('example.db')
c = conn.cursor()

# テーブルの作成
c.execute('''CREATE TABLE IF NOT EXISTS users
            (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# データの挿入
if st.button("データを挿入"):
    c.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25))
    conn.commit()
    st.write("データが挿入されました")
 
# データの取得
c.execute("SELECT * FROM users")
rows = c.fetchall()
 
# データの表示
st.write("ユーザー情報:")
for row in rows:
    st.write(row)
 
# 接続を閉じる
conn.close()"""