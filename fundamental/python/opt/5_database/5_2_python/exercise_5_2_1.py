# 注意
# 本演習を始める前に、教材に従って、テストデータベースおよびテーブルを作成してください。
# また、作成後にデータベースにテストデータをテーブルに挿入してください。

# PostgreSQL接続用のコネクションインスタンスを返す関数を作成してください。
# reference :
#  - https://www.psycopg.org/docs/module.html#psycopg2.connect

import psycopg2


def generate_postgresql_instance():
    # DataBase名を記入してください。
    dbname = "python_sql_exercise_db"
    # DataBaseホストを記入してください。(IPアドレスです)
    dbhost = ""
    # DataBaseのポートを記入してください。
    dbport = ""
    # DataBase名を使えるユーザ名を記入してください。
    dbuser = ""
    # 上記ユーザ名のパスワードを記入してください。
    dbpass = ""

    conn = psycopg2.connect(
        dbname=dbname, user=dbuser, password=dbpass, host=dbhost, port=dbport
    )

    return conn