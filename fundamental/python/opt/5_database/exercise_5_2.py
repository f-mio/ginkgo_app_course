# 前回の演習問題データを使用して、データベースのテーブルの中身を表示してみましょう。

from exercise_5_1 import generate_postgresql_instanse
import psycopg2

# 下記にプログラムを記載していってください。

postgre_instanse = generate_postgresql_instanse()


def first_select_query(instanse: psycopg2):
    # 下記にクエリを記述してください。
    sql = ""

    with instanse.cursor() as cur:
        cur.execute(sql)
        output = cur.fetchall()

    print(output)


if __name__ == '__main__':
    first_select_query(postgre_instanse)