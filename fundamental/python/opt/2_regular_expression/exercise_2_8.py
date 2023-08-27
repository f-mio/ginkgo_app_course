"""
[数値入力時の例外処理]
exercise_1_1_3で作成したメソッドの改良を行います。

[要件]
  - inputを使って、数字を入力してその数字を2倍にする関数を作成して下さい。
  - input_value_to_2times_value2内にinputを判定するメソッドを実装する
    - 先頭に、【+】, 【-】が入っている場合はOK
    - 小数点が数字の後に入っている場合はOK
    - 数字以外の文字列が入力された場合エラーを出力する
    - 【,】が入っている場合もエラー
"""

# 下記にプログラムを書いて下さい。
def input_value_to_2times_value2(input_value: str):
    pass


if __name__ == '__main__':
    input_value = input("数値を入力してください")

    # inputの値をinput_valueに代入
    print(input_value_to_2times_value2(input_value))

    pass