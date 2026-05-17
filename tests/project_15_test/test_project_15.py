import pytest
from project_15.script_project_15 import validate_input, sanitize_input, reverse_str


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("My name is ", ["My", "name", "is"]),
        (" Nice to meet you ", ["Nice", "to", "meet", "you"]),
        ("12345", ["12345"]),
        ("no yes yes no", ["no", "yes", "yes", "no"]),
        ("12  345", ["12", "345"]),
        ("         abc defg", ["abc", "defg"]),
    ],
)
def test_sanitize_input(input_str: str, expected: list[str]):
    assert sanitize_input(input_str) == expected


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("My name is", True),
        ("Nice to meet you", True),
        ("12345", True),
        ("", False),
    ],
)
def test_validate_input(input_str: str, expected: bool):
    assert validate_input(input_str) == expected


@pytest.mark.parametrize(
    "word_list, expected",
    [
        (["race", "car"], "car race"),
        (["12345"], "12345"),
        (["12", "345"], "345 12"),
        (["My", "name", "is"], "is name My"),
    ],
)
def test_reversed_str(word_list: list[str], expected: str):
    assert reverse_str(word_list) == expected
