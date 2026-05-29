import pytest
from project_23.script_project_23 import (
    validate_input,
    sanitize_input,
    read_file,
    find_overlapping_numbers,
    display_overlapping_numbers,
)


@pytest.mark.parametrize(
    "raw, expected", [(" 1 ", "1"), ("\t2\n", "2"), (" 3  ", "3"), ("abc", "abc")]
)
def test_sanitize_input(raw, expected):
    assert sanitize_input(raw) == expected


@pytest.mark.parametrize(
    "user_input, expected",
    [
        ("y", "y"),
        ("yes", "y"),
        ("n", "q"),
        ("no", "q"),
        ("", "y"),
        ("q", "q"),
        ("quit", "q"),
        ("123", "invalid"),
    ],
)
def test_validate_input(user_input, expected):
    assert validate_input(user_input) == expected


def test_read_file(tmp_path):
    # Define isolated directory
    file_path = tmp_path / "test_file.txt"

    # Test file does not exist
    assert read_file(str(file_path)) == set()

    # Create a temp file on disk
    file_path.write_text("1\n2\n3", encoding="utf-8")

    # Test file exists
    assert read_file(str(file_path)) == {1, 2, 3}


@pytest.fixture()
def sample_data():
    """Sample sets of integers."""
    prime_numbers = {
        2,
        3,
        5,
        7,
        11,
        13,
        17,
        19,
        23,
        29,
        31,
        37,
        41,
        43,
        47,
        53,
        59,
        61,
        67,
        71,
        73,
        79,
        83,
        89,
        97,
    }
    happy_numbers = {
        1,
        7,
        10,
        13,
        19,
        23,
        28,
        31,
        32,
        44,
        49,
        68,
        70,
        79,
        82,
        86,
        91,
        94,
        97,
    }
    return prime_numbers, happy_numbers


def test_find_overlapping_numbers(sample_data):
    prime_numbers, happy_numbers = sample_data
    assert find_overlapping_numbers(prime_numbers, happy_numbers) == [
        7,
        13,
        19,
        23,
        31,
        79,
        97,
    ]


def test_display_overlapping_numbers():
    assert (
        display_overlapping_numbers([1, 2, 3]) == "The overlaping numbers are [1, 2, 3]"
    )
    assert display_overlapping_numbers([]) == "The overlaping numbers are []"
