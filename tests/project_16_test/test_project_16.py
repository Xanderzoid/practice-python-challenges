import pytest
from project_16.script_project_16 import (
    sanitize_input,
    sanitize_type,
    validate_input,
    strong_pass,
    weak_pass,
    analysis_entropy,
)


@pytest.mark.parametrize(
    "input_str, expected",
    [(" Yes ", True), ("y", True), ("strong", True), ("", False), ("No", False)],
)
def test_sanitize_type(input_str, expected):
    assert sanitize_type(input_str) == expected


@pytest.mark.parametrize(
    "input_str, expected", [(" 10 ", 10), ("5.5", 0), ("7", 0), ("26", 0)]
)
def test_sanitize_input(input_str: str, expected: str):
    assert sanitize_input(input_str) == expected


@pytest.mark.parametrize(
    "input_dict, expected",
    [
        ({"weak": True, "strong": False, "length": 10}, True),
        ({"weak": False, "strong": True, "length": 16}, True),
        ({"weak": False, "strong": True, "length": 0}, False),
        ({"weak": False, "strong": True, "length": 7}, False),
    ],
)
def test_validate_input(input_dict: dict[str, int | bool], expected: bool):
    assert validate_input(input_dict) == expected


@pytest.mark.parametrize("input_int, expected", [(8, 8), (15, 15), (20, 20)])
def test_strong_pass(input_int: int, expected: int):
    password = strong_pass(input_int)["password"]
    assert len(password) == expected
    for x in password:
        assert 33 <= ord(x) <= 126


def test_weak_pass():
    assert len(weak_pass()["password"]) == 8


@pytest.mark.parametrize(
    "input_dict, expected",
    [
        ({"R": 93, "L": 16}, 104.63),
        ({"R": 93, "L": 10}, 65.39),
        ({"R": 26, "L": 8}, 37.6),
    ],
)
def test_anlaysis_entropy(input_dict: dict[str, int], expected: float):
    assert analysis_entropy(input_dict) == expected
