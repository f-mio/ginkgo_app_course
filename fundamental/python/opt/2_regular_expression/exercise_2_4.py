
# 正規表現を学習します。
# 日付の正規表現パターンを作成してください。
# 日付は以下の形式で表されます：YYYY/MM/DD
# 返り値はBool型にして下さい。


# 下記にプログラムを記載して下さい。

sample = "2023/08/1"

def is_datetime_format(letter: str):
    pass

if __name__ == '__main__':
    if (is_datetime_format(sample)):
        print(f"{sample}は日付のフォーマットです。")
    else:
        print(f"{sample}は日付のフォーマットではありません。")