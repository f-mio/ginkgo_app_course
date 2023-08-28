
import pytest

from exercise_2_1 import has_letter_abc
from exercise_2_2 import has_letter_2byte_space
from exercise_2_3 import is_phone_number
from exercise_2_4 import is_datetime_format
from exercise_2_5 import search_char_period
from exercise_2_6 import is_numeric_str
from exercise_2_7 import is_english_letter


class TestExercise2_1():
    ok_case = (
        "abc", "badsaytasabcewa", "AebabcW"
    )
    ng_case = (
        "ａｂｃ", "aｂｃ", "ABc", "Hi, Mike."
    )
    @pytest.mark.parametrize('letter', ok_case)
    def letter_include_abc_return_true(self, letter):
        assert has_letter_abc(letter)

    @pytest.mark.parametrize('letter', ng_case)
    def letter_does_not_have_abc_return_false(self, letter):
        assert not has_letter_abc(letter)


class TestExercise2_2():
    ok_case = (
        "全角スペース【　】が含まれています。",
        "あ　い　う。"
    )
    ng_case = (
        "Does not exist 2byte space.",
        "半角スペース【 】が含まれています。"
    )
    @pytest.mark.parametrize('letter', ok_case)
    def letter_include_2byte_space_return_true(self, letter):
        assert has_letter_2byte_space(letter)

    @pytest.mark.parametrize('letter', ng_case)
    def letter_does_not_have_2byte_space_return_false(self, letter):
        assert not has_letter_2byte_space(letter)


class TestExercise2_3():
    pass


class TestExercise2_4():
    pass


class TestExercise2_5():
    ok_case = (
        "My laptop pc is bought 5 years ago.",
        ".",
        "ses cource."
        )

    ng_case = (
        "My pen．", "a", "")

    @pytest.mark.parametrize('letter', ok_case)
    def test_letter_included_period_should_return_true(self, letter):
        assert search_char_period(letter)

    @pytest.mark.parametrize('letter', ng_case)
    def test_letter_not_included_period_should_return_false(self, letter):
        assert search_char_period(letter) == False