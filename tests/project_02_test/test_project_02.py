import pytest
from project_02.script_project_02 import result_msg, validate_input, identify_even


def test_result_msg():
    even_num = 2
    odd_num = 3
    result_even = result_msg(True, even_num)
    result_odd = result_msg(False, odd_num)
    assert result_even == f"The number {even_num} is even.\n"
    assert result_odd == f"The number {odd_num} is odd.\n"


def test_validate_input(monkeypatch):
    inputs = iter(["abc", "9"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = validate_input()
    assert result == 9.0


def test_identify_even():
    num_list = [1, 2, 3, 4]
    bool_list = [False, True, False, True]
    result_list = [identify_even(x) for x in num_list]
    assert result_list == bool_list
