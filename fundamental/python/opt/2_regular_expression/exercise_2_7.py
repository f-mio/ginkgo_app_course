
# 正規表現を学習します。
# 英語の文章であるかどうかを判定してください。
# 英語の文章は、大文字の英数字で始まり、ピリオドで終わる形式です。
# 返り値はBool型にして下さい。


# 下記にプログラムを記載して下さい。

sample = "Studying python 3years."

def is_english_letter(letter: str):
    pass

if __name__ == '__main__':
    if (is_english_letter(sample)):
        print(f"{sample}は英文です。")
    else:
        print(f"{sample}は英文のフォーマットではありません。")