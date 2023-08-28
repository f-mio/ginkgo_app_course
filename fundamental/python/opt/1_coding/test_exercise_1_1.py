
import pytest

from exercise_1_1_2 import decolate_name_to_hello_name
from exercise_1_1_3 import input_value_to_2times_value


class TestExercise1_1_2():
    correct_pair = (
        ("aaaa", "Hello aaaa!"),
        ("Taro", "Hello Taro!")
        )
    @pytest.mark.parametrize('input, expect', correct_pair)
    def test_input_name_then_decorated_string(self, input, expect):
        result = decolate_name_to_hello_name(input)
        assert expect == result

class TestExercise1_1_3():
    correct_pair = (
        ("1", 2), ("2", 4), ("1.5", 3),
    )

    @pytest.mark.parametrize('input, expect', correct_pair)
    def test_if_input_numeric_should_return_2_times_value(self, input, expect):
        result = input_value_to_2times_value(input)
        assert expect == result
