/*
新しいテーブルを作成したいと思います。
各国の都市名を格納したcityテーブルです。
公式ページ,前回までの結果と要件を参考にテーブルを作成してください。
  - https://www.postgresql.jp/document/14/html/sql-createtable.html

[要件]
  - データベースfirst_db内に作成すること
  - テーブル名はcityであること
  - カラムは下記を持っていること
    - id SERIAL NOT NULL PRIMARY KEY
    - city VARCHAR(50)
    - country_id INTEGER (違和感を持った方もこの章はこのまま進めてください)
    - is_capital BOOLEAN (首都かどうかを表す)
    - create_timestamp TIMESTAMP
*/
