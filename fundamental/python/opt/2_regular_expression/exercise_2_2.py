
# 正規表現を学習します。
# プログラミングにおいて全角スペースが入っているとエラーが起きる場合が有ります。
# 任意の文字列が与えられた場合、全角スペースが入っていることを判定する関数を作成して下さい。
# 返り値はBool型にして下さい。


# 下記にプログラムを記載して下さい。

sample_letter = "This letter include 　."

def has_letter_2byte_space(letter: str):
    pass

if __name__ == '__main__':
    if (has_letter_2byte_space(sample_letter)):
        print(f"{sample_letter}には全角スペースが含まれています。")
    else:
        print(f"{sample_letter}には全角スペースが含まれていません。")