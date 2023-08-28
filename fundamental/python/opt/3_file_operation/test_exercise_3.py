import pytest
import re
from glob import glob

from exercise_3_1 import txt_file_cnt
from exercise_3_2 import txt_file_named_correct_cnt
from exercise_3_3 import txt_file_named_c_dot_t_cnt

class TestExercise3_1():
    def test_txt_file_cnt_return_correct_cnt_value(self):
        correct = len(glob("./**/*.txt", recursive=True))
        result = txt_file_cnt()
        assert correct == result

class TestExercise3_2():
    def test_txt_file_named_correct_cnt(self,):
        result = txt_file_named_correct_cnt()
        all_txt_files = glob("./**/*.txt", recursive=True)
        cnt = 0
        for path in all_txt_files:
            if re.search("correct.+¥.txt$"):
                cnt += 1
        assert cnt == result

class TestExercise3_3():
    def test_txt_file_named_correct_cnt(self,):
        result = txt_file_named_c_dot_t_cnt()
        all_txt_files = glob("./**/*.txt", recursive=True)
        cnt = 0
        for path in all_txt_files:
            if re.search("c\.t\.txt$"):
                cnt += 1
        assert cnt == result

