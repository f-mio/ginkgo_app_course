"""
[deep copy and sharrow copy]
templateであるinput_listに変更を加えず、input_listをコピーしたもので
   output = [0, 1, 2, 3]
となるものを作成してください。
下記にプログラムを書いて下さい。
"""

input_list = [0, 1, 1, 2]


def list_copy(input_list: list) -> list:
    # inputリストのコピーを作成してください。

    # ここでコピーしたもの2番目の値を2に入れ替えてください。

    return output


if __name__ == '__main__':

    # inputの値をinput_valueに代入
    output = list_copy(input_list)

    print('出力結果は下記のとおりです。')
    print(f"input  : {input_list}")
    print(f"output : {output}")