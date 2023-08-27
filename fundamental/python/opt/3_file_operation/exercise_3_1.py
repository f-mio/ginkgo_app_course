"""
[ファイル読み込みの例外処理1]
存在しないデータをインポートした際にエラーを返すメソッドを作成して下さい。
[要件]
 - 読み込み対象はcsvファイル
 - 読み込めた場合は、csvファイルの内容をコンソールに出力する
 - 存在しないファイルがあった場合はコンソールに「ファイルが存在しません」というメッセージを出力してプログラムを終了する。
"""
def import_csv_data_and_output(input_list: list):
    pass

exist_file_path = "./csv_and_log_data/import_data.csv"
none_exist_file = "./none_exist_file.csv"

if __name__ == '__main__':
    # ファイルが存在した場合の処理
    import_csv_data_and_output(exist_file_path)
    # ファイルが存在しなかった場合の処理
    import_csv_data_and_output(none_exist_file)