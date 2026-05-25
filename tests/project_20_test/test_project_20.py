import pytest
from project_20.script_project_20 import (
    sanitize_input,
    validate_input,
    gen_num_list,
    binary_search,
    modify_list,
)


@pytest.mark.parametrize(
    "raw, expected",
    [
        (" 1 ", "1"),
        ("\t2\n", "2"),
        (" 3  ", "3"),
        ("abc", "abc"),
    ],
)
def test_sanitize_input(raw, expected):
    assert sanitize_input(raw) == expected


@pytest.mark.parametrize(
    "user_input, expected",
    [
        ("1", True),
        ("99", True),
        ("100", True),
        ("abc", False),
        ("sd1", False),
        ("", False),
    ],
)
def test_validate_input(user_input, expected):
    assert validate_input(user_input) == expected


def test_gen_num_list():
    num_list = gen_num_list(10)
    assert len(num_list) == 10
    assert all(isinstance(num, int) for num in num_list)


@pytest.mark.parametrize(
    "arr, target, expected",
    [
        ([1, 3, 5, 7, 9], 5, 2),
        ([1, 3, 5, 7, 9], 6, 3),
        ([1, 3, 5, 7, 9], 0, 0),
        ([1, 3, 5, 7, 9], 10, 5),
    ],
)
def test_binary_search(arr, target, expected):
    assert binary_search(arr, target) == expected


@pytest.mark.parametrize(
    "arr, target, index, expected",
    [
        ([1, 3, 5, 7, 9], 5, 2, [1, 3, 5, 5, 7, 9]),
        ([1, 3, 5, 7, 9], 6, 3, [1, 3, 5, 6, 7, 9]),
        ([1, 3, 5, 7, 9], 0, 0, [0, 1, 3, 5, 7, 9]),
        ([1, 3, 5, 7, 9], 10, 5, [1, 3, 5, 7, 9, 10]),
    ],
)
def test_modify_list(arr, target, index, expected):
    assert modify_list(arr, target, index) == expected
