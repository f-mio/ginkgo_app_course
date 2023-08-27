/*
ビューの作成
テーブル同士を結合して、扱いやすいようにする方法の一つにViewがあります。
countryとcityをleft joinで結合したビューファイルを作成してください。
下記のページを参考に作成してください。
 - https://www.postgresql.jp/document/14/html/sql-createview.html
[要件]
 - ビューのカラムは下記のようにしてください。
   - city_id : cityテーブルのID
   - country_id : countryテーブルのID
   - country_name : countryテーブルのcountry(国名)
   - city_name : cityテーブルのcity(都市名)
*/