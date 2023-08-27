"""
heritageテーブルでcreation_year_strを作りましたが、文字列なので使い勝手が悪いです。
まずはソートをできるように整数型のカラムを準備したいです。
過去の演習や公式ドキュメントを参考にして、新しいカラムを定義してください。
要件は下記です。

[要件]
 - テーブル名 : heritage
 - creation_year : レコードの書き込み時刻
"""

from exercise_5_2_1 import generate_postgresql_instance
import psycopg2


def add_creation_year_column_query():
    # 下記にクエリを記述してください。
    sql = ""

    conn = generate_postgresql_instance()
    with conn.cursor() as cur:
        cur.execute(sql)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    add_creation_year_column_query()
