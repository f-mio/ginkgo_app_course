"""
[テストドリブン2]
e-mailアドレスを入力させるプログラムを作成して下さい。
入力ルールから外れるものについてはエラーを出すようにして下さい。
この問題は、テストコード実行が通った場合に合格になります。
[テストコード実行方法]
 # cd /workdir/opt/6_test_code
 # python -m pytest test_exercise_6.py::TestExercise6_2
[要件]
  - 入力されたemailアドレスを検証する関数
  - emailアドレスが正しい場合は何も返さない
  - emailアドレスが間違っている場合はexceptionを発生させる
  - 正しいアドレスの条件
    - 1文字目が英字であること
    - 2文字目以降が、英字もしくは数字であること
    - @以前が5文字以上であること
    - @が含まれること
    - ドメインに.jp, もしくは.comが含まれ、このどちらかで終わっていること。
"""

def validate_email(email: str) -> None:
    """
    description
    --------
    正しいEmailアドレスが入力された場合、何も返さず、
    正しくないEmailアドレスが入力された場合、上位メソッドにエラーを
    発生させるメソッド

    input
    --------
    email : string

    output
    --------
    None

    exception
    --------
     - emailにstr以外が入った場合
         エラー文 ： 【入力はstr型のみ有効です。】
     - 入力ルール以外のものが入ってきた場合にExceptionを発生させること。
         エラー文 ： 【emailアドレスが正しくありません。】

    入力ルール
    --------
     - 1文字目が英字であること
     - 2文字目以降が、英字もしくは数字であること
     - @以前が5文字以上であること
     - @が含まれること
     - ドメインに.jp, もしくは.comが含まれ、このどちらかで終わっていること。
    """
    pass



if __name__ == '__main__':
    email = input("emailを入力して下さい ： ")
    if validate_email(email):
        print(f"入力したemail : {email}は正しい形です。")
    else:
        print(f"入力したemail : {email}は誤った形です。")