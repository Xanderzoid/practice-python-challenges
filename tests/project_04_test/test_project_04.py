import pytest
from project_04.script_project_04 import (
    validate_input,
    cal_divisors,
)


def test_validate_input(monkeypatch):
    inputs = iter(["abc", "20"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = validate_input()
    assert result == 20


def test_cal_divisors():
    numbers = [1, 5, 20]
    expected_list = [[1], [1, 5], [1, 2, 4, 5, 10, 20]]

    result_list = []
    for num in numbers:
        result = cal_divisors(num)
        result_list.append(result)
    assert result_list == expected_list
