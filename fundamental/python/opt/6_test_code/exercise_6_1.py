"""
[テストドリブン1]
xの二乗を返す関数を作成してください。
この問題は、テストコード実行が通った場合に合格になります。
[テストコード実行方法]
 # cd /workdir/opt/6_test_code
 # python -m pytest test_exercise_6.py::TestExercise6_1
[要件]
 - 入力した数の二乗を返す関数
 - int,float以外が入力された場合、ValueErrorを発行する。
"""

def func_power2(x: int | float) -> float | int:
    """
    input
    --------
    x : float

    output
    --------
    result : float

    exception
    --------
     - ValueError : xにintまたはfloat以外が型が引数内に入った場合 (有理数、無理数も弾く)
    """
    pass


