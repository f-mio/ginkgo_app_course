import numpy as np

import pytest

from func_execise_1 import func_power2

# テストケース


ok_case = (0, 1, 2, 3.4, np.pi)
ng_case = ("1", [1, 2], {2})

class TestExecise1():

    @pytest.mark.parametrize('x', ok_case)
    def test_numeric_argument_should_return_power_2_value(self, x):

        result = func_power2(x)

        assert (result == x**2)

    @pytest.mark.parametrize('x', ng_case)
    def test_not_numeric_argument_should_raise_TypeError_exception(self, x):

        with pytest.raises(TypeError) as e:
            _ = func_power2(x)

        assert (e.value.args[0] == "数値以外の入力は受け付けません。")