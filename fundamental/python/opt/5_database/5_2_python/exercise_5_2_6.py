"""
heritageテーブルで先ほどの問題でcreation_yearを作りました。
ここに数値を入れたいと思います。
要件に従ってUPDATEクエリを作成してください。

[要件]
 - テーブル名 : heritage
 - creation_year_strのデータ加工
   - 紀元前のデータは、-を頭につける　(紀元前1600年だと、-1600)
   - 世紀と含まれるものは100年単位で数値化する。　(西暦7世紀→600、紀元前10世紀→-1000)
[ヒント]
 1.一度selectで、idとcreation_year_strを取得
 2.正規表現で中身を加工してupdateクエリを実行
"""

from exercise_5_2_1 import generate_postgresql_instance
import psycopg2


def update_creation_year_query():
    # 下記にクエリを記述してください。
    sql = ""

    conn = generate_postgresql_instance()
    with conn.cursor() as cur:
        cur.execute(sql)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    update_creation_year_query()
