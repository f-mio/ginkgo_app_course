"""
[例外処理1]
リストを入力して、
 - 一番初めの値がint型ならtrueを返す関数を作成してください。
 - それ以外の場合はFalseを返してください。
 - リスト以外の型が入力された場合はExceptionを発生させてください。
   (Exceptionのメッセージは、"型がリストではありません。"としてください)
下記にプログラムを書いて下さい。
"""
def list_type_checker(input_list: list):
    pass

sample_list = ['一番目', '二番目', '三番目']

if __name__ == '__main__':

    output = list_type_checker(sample_list)
    print(output)
    error_output = list_type_checker('text')