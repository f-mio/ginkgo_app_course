/*
二つのテーブルを作成しました。countryとcityテーブルはそれぞれ関係しているテーブルです。
関係しているテーブル間では、クエリで結合して一つのテーブルのように表示することができます。
left joinを用いて二つのテーブルを結合したものを表示するSELECT文を作成してください。
なお、fromで取得するテーブルはcountryとして下さい。
下記のページを参考に作成してください。
 - https://www.postgresql.jp/document/14/html/sql-select.html

[要件]
 - 表示するカラムは下記のようにしてください。
   - city_id : cityテーブルのID
   - country_id : countryテーブルのID
   - country_name : countryテーブルのcountry(国名)
   - city_name : cityテーブルのcity(都市名)

また前回作成したinner joinとleft joinの違いを確認してみてください。
*/
