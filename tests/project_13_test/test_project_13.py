import pytest
from project_13.script_project_13 import parse_and_validate, get_fibonacci_sequence


def test_parse_and_validate():
    assert parse_and_validate("10") == 10
    assert parse_and_validate("q") == 0
    assert parse_and_validate(" Quit ") == 0


def test_parse_and_validate_invalid():
    with pytest.raises(ValueError):
        parse_and_validate("25")
    with pytest.raises(ValueError):
        parse_and_validate("Word")


def test_get_fibonacci_sequence():
    assert list(get_fibonacci_sequence(5)) == [1, 1, 2, 3, 5]
    assert list(get_fibonacci_sequence(1)) == [1]
