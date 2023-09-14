
import pytest

from exercise_1_6_1 import list_type_checker

class TestExercise1_6_1():
    true_pattern = (
        [1, 2, 3], [3, "2",],
    )
    false_pattern = (
        ["1", 2, 3], [0.3, 1, 1],
        [["1", "second", 3], "second"],
        ['', None, ],
    )
    error_case = (
        'a', 23, 1.23,
        (1,2,3), ("1", "2"),
        {}, {"a": 1, "b": 2},
        {1,2,3}
    )

    @pytest.mark.parametrize('input_list', input_list)
    def test_return_true(self, input_list):
        resut = list_type_checker(input_list)
        assert result

    @pytest.mark.parametrize('input_list', input_list)
    def test_return_false(self, input_list):
        resut = list_type_checker(input_list)
        assert not result

    @pytest.mark.parametrize('error_input', error_case)
    def test_not_list_input_should_raise_exception(self, error_input):
        with pytest.raises(Exception) as e:
            _ = list_type_checker(error_input)

        assert e.value.args[0] == "型がリストではありません。"