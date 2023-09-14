import numpy as np

import pytest

from exercise_6_1 import func_power2
from exercise_6_2 import validate_email

###
# テストケース
# 6_1
ok_case_6_1 = (0, 1, 2, 3.4)
ng_case_6_1 = ("1", [1, 2], {2}, np.pi)

# 6_2
ok_case_6_2 = (
    "Ez123@ginkgo.jp", "dkudo@ginkgo.com"
)
ng_case_6_2_1 = (
    1111, ["python",], ["validEmail@ginkgo.com", "validEmail2@ginkgo.jp"],
    {"validEmail@g.jp"}
)
ng_case_6_2_2 = (
    "a@gmail.com", "12345@gmai.com",
    "t53@gmail.jp", "abcdef@g.jp.bz",
    "d.kudo@ginkgo.com",
)


class TestExercise6_1():
    """
    exercise_6_1のテスト
    """

    @pytest.mark.parametrize('x', ok_case_6_1)
    def test_numeric_argument_should_return_power_2_value(self, x):

        result = func_power2(x)

        assert (result == x**2)

    @pytest.mark.parametrize('x', ng_case_6_1)
    def test_not_numeric_argument_should_raise_TypeError_exception(self, x):

        with pytest.raises(TypeError) as e:
            _ = func_power2(x)

        assert (e.value.args[0] == "数値以外の入力は受け付けません。")


class TestExercise6_2():
    """
    exercise_6_2のテスト
    """

    @pytest.mark.parametrize('email', ok_case_6_2)
    def test_valid_email_should_return_none(self, email):
        """
        通りのメールアドレスが入力された場合、noneが返ることを確認。
        """

        result = validate_email(email)

        assert result is None


    @pytest.mark.parametrize('email', ng_case_6_2_1)
    def test_invalid_email_should_raise_exception(self, email):
        """
        要件から外れるメールアドレスが入力された場合エラーを出すことの確認。
        """

        with pytest.raises(Exception) as e:
            _ = validate_email(email)

        assert (e.value.args[0] == "入力はstr型のみ有効です。")


    @pytest.mark.parametrize('email', ng_case_6_2_2)
    def test_invalid_email_should_raise_exception(self, email):
        """
        要件から外れるメールアドレスが入力された場合エラーを出すことの確認。
        """

        with pytest.raises(Exception) as e:
            _ = validate_email(email)

        assert (e.value.args[0] == "emailアドレスが正しくありません。")