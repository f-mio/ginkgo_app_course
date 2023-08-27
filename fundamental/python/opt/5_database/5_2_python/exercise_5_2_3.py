"""
5_1の問題を参考に、テーブルを作成してください。
また、SQL発行後に、ALTER TABLEクエリでcityテーブルとリレーションを設定してください。
(city.idとheritage.city_idです)
要件は下記です。

[要件]
 - テーブル名 : heritage
 - カラム
    - id SERIAL NOT NULL PRIMARY KEY
    - country_id INTEGER
    - heritage VARCHAR(50)
    - creation_year_str VARCHAR(10)
    - create_timestamp TIMESTAMP
"""

from exercise_5_2_1 import generate_postgresql_instance
import psycopg2


def create_table_query():
    # 下記にクエリを記述してください。
    sql = ""

    conn = generate_postgresql_instance()
    with conn.cursor() as cur:
        cur.execute(sql)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    create_table_query()
