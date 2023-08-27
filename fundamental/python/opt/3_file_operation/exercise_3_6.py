"""
[ログ出力]
importデータを読み込み、変数内に保管してから、リストにデータを追加して新しいcsvファイルを作成して下さい。
[要件]
  - exercise_3_1の変数を使用
  - ログ出力ファイル名 : log_data.log
  - 正常ケースでの保存する内容 : タブ形式で、"実行時間"\t"成功"\t"実行ファイル名"\t"パス名"\n
  - 正常ケースでの保存する内容 : タブ形式で、"実行時間"\t"失敗"\t"実行ファイル名"\t"エラー文"\n
[ヒント]
pythonでログ保存を行う場合は標準モジュールのloggingを使用することができます。
https://docs.python.org/ja/3/library/logging.html
また、エラーパターンはそのままやったらログに保存されないので適切に例外処理を入れて下さい。
"""

from exercise_3_1 import import_csv_data_and_output

# logファイル名
log_file_name = './csv_and_log_data/log_data.log'
# 入力ファイル名
import_file = './csv_and_log_data/import_data.csv'
none_exist_file = "./none_exist_file.csv"


# loggingのインスタンス設定


# 正常時のファイル実行


# 異常時のファイル実行


