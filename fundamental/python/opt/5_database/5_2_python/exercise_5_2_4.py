"""
PostgreSQLのサイトを参考に、heritageテーブルにレコードを挿入してください。
要件は下記です。

[要件]
 - テーブル名 : heritage
 - レコード1
    - country_id : 1
    - heritage : "名古屋城"
    - creation_year_str : "1610年"
    - create_timestamp : レコードの書き込み時刻
 - レコード2
    - city_id : 1
    - heritage : "八幡山古墳"
    - creation_year_str : "5世紀"
    - create_timestamp : レコードの書き込み時刻
 - レコード3
    - city_id : 2
    - heritage : "八達嶺長城"
    - creation_year_str : "紀元前7世紀"
    - create_timestamp : レコードの書き込み時刻
"""

from exercise_5_2_1 import generate_postgresql_instance
import psycopg2


def insert_record_query():
    # 下記にクエリを記述してください。
    sql = ""

    conn = generate_postgresql_instance()
    with conn.cursor() as cur:
        cur.execute(sql)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    record1 = {
        "city_id" : 2,
        "heritage" : "名古屋城",
        "creation_year_str" : "1610年",
        "create_timestamp" : "NOW()"
    }
    record2 = {
        "city_id" : 2,
        "heritage" : "八幡山古墳",
        "creation_year_str" : "5世紀",
        "create_timestamp" : "NOW()"
    }
    record3 = {
        "city_id" : 3,
        "heritage" : "八達嶺長城",
        "creation_year_str" : "紀元前7世紀",
        "create_timestamp" : "NOW()"
    }

    insert_record_query(record1)
    insert_record_query(record2)
    insert_record_query(record3)
