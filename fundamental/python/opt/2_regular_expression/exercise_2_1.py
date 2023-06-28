
# 正規表現を学習します。
# 任意の文字列が与えられた場合、abcという文字列が含まれているかどうかを判定する関数を作成して下さい。
# 返り値はBool型にして下さい。


# 下記にプログラムを記載して下さい。

sample_letter = "aaabcefg"


def has_letter_abc(letter: str):
    pass


if __name__ == '__main__':
    if has_letter_abc(sample_letter):
        print(f"{sample_letter}にはabcが含まれています。")
    else:
        print(f"{sample_letter}にはabcが含まれていません。")