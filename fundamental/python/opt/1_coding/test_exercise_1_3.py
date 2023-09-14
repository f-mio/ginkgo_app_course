
import pytest

from exercise_1_3_1 import return_second_element
from exercise_1_3_2 import transform_second_element_to_str
from exercise_1_3_3 import list_copy
from exercise_1_3_4 import animal_dict_handling

class TestExercise1_3_1():
    input_and_expect = (
        ([1, 2, 3], 2),
        (["1", 2, 3], 2),
        (["1", "second", 3], "second"),
        (['', None, ], None),
    )

    @pytest.mark.parametrize('input_list, expect', input_and_expect)
    def test_return_second_element(self, input_list, expect):
        result = return_second_element(input_list)
        assert result == expect


class TestExercise1_3_2():
    input_list = (
        ["1", "2", "3",],
        [1, 2, 3,],
        ["str", 3.4, 3/4],
    )

    @pytest.mark.parametrize('input_list', input_list)
    def test_second_element_in_output_should_be_str(self, input_list):
        result = transform_second_element_to_str(input_list)
        assert isinstance(result[1], str)


class TestExercise1_3_3():
    input_dict = ({
        '犬': 'dog',
        'ライオン': 'lions'
        }, )

    @pytest.mark.parametrize("input_dict", input_dict)
    def test_animal_dict_handling(self, input_dict):
        result = animal_dict_handling(input_dict)
        assert (
            result["猫"] == "cats"
            and result["犬"] == "dogs"
            )


class TestExercise1_3_4():
    input_list = (
        [0, 1, 1, 2],
        )

    @pytest.mark.parametrize("input_list", input_list)
    def test_list_copy(self, input_list):
        result = list_copy(input_list)

        assert (
            input_list != result
            and result[1] == 2
        )

