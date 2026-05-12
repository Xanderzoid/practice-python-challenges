import builtins
import pytest
from project_12.script_project_12 import (
    validate_input,
    generate_list,
    remove_first_last,
)


@pytest.mark.parametrize(
    "input_str, expected",
    [("start", "y"), ("EXIT", "q"), ("  next  ", "y"), ("no", "q")],
)
def test_validate_input_variants(input_str, expected):
    assert validate_input(input_str) == expected


def test_generate_list():
    length = 10
    test_list = generate_list(length)
    assert length == len(test_list)
    for i in test_list:
        assert isinstance(i, int)


def test_remove_first_last():
    list_01 = [1, 2, 3]
    list_02 = [0, 0, 2, 100]
    assert remove_first_last(list_01) == [1, 3]
    assert remove_first_last(list_02) == [0, 100]
    assert remove_first_last([5]) == [5, 5]
    assert len(remove_first_last(list_01)) == 2
