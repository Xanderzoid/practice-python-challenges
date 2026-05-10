import pytest
from datetime import date
from project_01.script_project_01 import (
    cal_century_year,
    birthday_message,
    get_valid_age,
)


@pytest.fixture
def sample_user_data():
    """Sample dictionary of the name and age of a user."""
    return {"name": "Xander", "age": 32}


def test_cal_century(sample_user_data):
    test_age = sample_user_data["age"]
    expected_year = date.today().year + (100 - test_age)

    result = cal_century_year(test_age)

    assert result == expected_year


def test_birthday_message(sample_user_data):
    expected_year = date.today().year + (100 - sample_user_data["age"])
    msg = birthday_message(sample_user_data["name"], expected_year)
    assert sample_user_data["name"] in msg
    assert str(expected_year) in msg


def test_get_valid_age_loop_recovery(monkeypatch, sample_user_data):
    """
    Tests that the loop recovers from bad input and returns the good one.
    We provide a list of inputs: first 'abc' (invalid), then '32' (valid).
    """
    inputs = iter(["abc", "32"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # This will now print the error for 'abc' and then return 32
    result = get_valid_age("Enter age: ")
    assert result == 32
