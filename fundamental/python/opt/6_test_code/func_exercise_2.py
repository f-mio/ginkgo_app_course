# e-mailアドレスを入力させるプログラムを作成して下さい。
# 入力ルールから外れるものについてはエラーを出すようにして下さい。

def validate_email(email: str) -> None:
    """
    description
    --------
    正しいEmailアドレスが入力された場合、何も返さず、
    正しくないEmailアドレスが入力された場合、上位メソッドにエラーを
    発生させるメソッド

    input
    --------
    None

    output
    --------
    email : string

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
    validate_email(email)
    print(f"入力したemail : {email}は正しい形です。")