import pytest
from project_18.script_project_18 import (
    validate_input,
    sanitize_input,
    four_digit_number,
    number_variance,
    user_commands,
)


@pytest.mark.parametrize(
    "raw_input, expected",
    [
        ("1234", True),
        ("1234", True),
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
    num_int = int(num)
    assert isinstance(num, str)
    assert 1000 <= num_int <= 9999


def test_number_variance():
    assert number_variance("1234", "1234")["cows"] == 0
    assert number_variance("1234", "1234")["bulls"] == 4
    assert number_variance("1234", "1432")["cows"] == 2
    assert number_variance("1234", "1432")["bulls"] == 2
    assert number_variance("1234", "5678")["cows"] == 0
    assert number_variance("1234", "5678")["bulls"] == 0
    assert number_variance("1234", "5612")["cows"] == 2
    assert number_variance("1234", "5612")["bulls"] == 0


@pytest.mark.parametrize(
    "user_input, expected",
    [
        ("r", {"rules": True, "quit": False, "invalid": False}),
        ("rules", {"rules": True, "quit": False, "invalid": False}),
        ("q", {"rules": False, "quit": True, "invalid": False}),
        ("quit", {"rules": False, "quit": True, "invalid": False}),
        ("exit", {"rules": False, "quit": True, "invalid": False}),
        ("invalid", {"rules": False, "quit": False, "invalid": True}),
    ],
)
def test_user_commands(user_input, expected):
    assert user_commands(user_input) == expected
