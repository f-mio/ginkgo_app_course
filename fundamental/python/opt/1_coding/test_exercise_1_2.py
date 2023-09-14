
import pytest

from exercise_1_2_1 import sum_of_3_args
from exercise_1_2_2 import power_2
from exercise_1_2_3 import divide_3
from exercise_1_2_4 import return_divide_3_remain
from exercise_1_2_5 import return_divide_3_quotinent


class TestExercise1_2_1():
    input_and_expect = (
        (1, 2, 3, 6),
        (2, 2, 2, 6),
        (1, 5, 10, 16),
    )

    @pytest.mark.parametrize('a,b,c, expect', input_and_expect)
    def test_3_int_arg_return_summersion(self, a, b, c, expect):
        resut = sum_of_3_args(a, b, c)
        assert result == expect


class TestExercise1_2_2():
    input_and_expect = (
        (2, 2*2),
        (3.5, 3.5**2),
        (1, 1),
        (3.33, 3.33**2)
    )

    @pytest.mark.parametrize('input, expect', input_and_expect)
    def test_power2(self, input, expect):
        result = power_2(input)
        assert result == expect


class TestExercise1_2_3():
    input_and_expect = (
        (2, 2/3),
        (3, 3/3),
        (0.5, 0.5/3)
    )

    @pytest.mark.parametrize('input, expect', input_and_expect)
    def test_divide_3(self, input, expect):
        result = divide_3(input)
        assert expect == result


class TestExercise1_2_4():
    input_and_expect = (
        (2, 2), (3, 0), (100, 1), (1, 1)
    )

    @pytest.mark.parametrize('input, expect', input_and_expect)
    def test_return_divide_3_remain(self, input, expect):
        result = return_divide_3_remain(input)
        assert expect == result


class TestExercise1_2_5():
    input_and_expect = (
        (2, 0), (3, 1), (100, 33), (1, 0),
        (4, 1), (20, 6)
    )

    @pytest.mark.parametrize('input, expect', input_and_expect)
    def test_return_divide_3_quotinent(self, input, expect):
        result = return_divide_3_quotinent(input)
        assert expect == result
