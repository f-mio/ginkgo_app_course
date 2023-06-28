
# 正規表現を学習します。
# 入力した文字列が電話番号かどうかを判定する関数を作成してください。
# 電話番号は以下の形式で表されます：(XXX) XXXX-XXXX
# 返り値はBool型にして下さい。


# 下記にプログラムを記載して下さい。

sample = "(070)1234-5678"

def is_phone_number(letter: str):
    pass

if __name__ == '__main__':
    if (is_phone_number(sample)):
        print(f"{sample}は電話番号です。")
    else:
        print(f"{sample}は電話番号のフォーマットではありません。")