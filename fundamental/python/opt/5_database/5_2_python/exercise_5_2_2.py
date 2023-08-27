"""
前回の演習問題データを使用して、データベースのテーブルの中身を表示してみましょう。
countryテーブルのレコードをid順に二つ取得し、コンソールに出力してください。
"""

from exercise_5_2_1 import generate_postgresql_instance
import psycopg2

def first_select_query():
    # 下記にクエリを記述してください。
    sql = ""

    conn = generate_postgresql_instance()
    with conn.cursor() as cur:
        cur.execute(sql)
        output = cur.fetchall()
    conn.close()

    print(output)


if __name__ == '__main__':
    first_select_query()
