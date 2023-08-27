"""
正規表現を学習します。
任意の文字列が与えられた場合、半角のピリオド【.】が含まれているかどうかを判定する関数を作成して下さい。
返り値はBool型にして下さい。
下記にプログラムを記載して下さい。
"""

sample_letter = "This letter include period."

def search_char_period(letter: str):
    pass

if __name__ == '__main__':
    if (search_char_period(sample_letter)):
        print(f"{sample_letter}には半角ピリオドが含まれています。")
    else:
        print(f"{sample_letter}には半角ピリオドが含まれていません。")