import pytest
from project_18.script_project_18 import (
    validate_input,
    sanitize_input,
    four_digit_number,
    number_variance,
)


@pytest.mark.parametrize(
    "raw_input, expected",
    [
        ("1234", True),
        (" 1234 ", True),
        ("abcd", False),
        ("12", False),
        ("12345", False),
        ("12a4", False),
    ],
)
def test_validate_input(raw_input, expected):
    assert validate_input(raw_input) == expected


@pytest.mark.parametrize(
    "raw_input, expected",
    [
        (" 1234 ", "1234"),
        ("\t1234\n", "1234"),
        (" 12 34 ", "1234"),
    ],
)
def test_sanitize_input(raw_input, expected):
    assert sanitize_input(raw_input) == expected


def test_four_digit_number():
    num = four_digit_number()
    assert isinstance(num, int)
    assert 1000 <= num <= 9999


def test_number_variance():
    assert number_variance(1234, 1234)["cows"] == 0
    assert number_variance(1234, 1234)["bulls"] == 4
    assert number_variance(1234, 1432)["cows"] == 2
    assert number_variance(1234, 1432)["bulls"] == 2
    assert number_variance(1234, 5678)["cows"] == 0
    assert number_variance(1234, 5678)["bulls"] == 0
    assert number_variance(1234, 5612)["cows"] == 2
    assert number_variance(1234, 5612)["bulls"] == 0
