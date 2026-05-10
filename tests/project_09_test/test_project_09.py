import pytest
from project_09.script_project_09 import validate_input, compare_num


def test_validate_input_type_valid():
    assert validate_input("1") == 1
    assert validate_input("4") == 4
    assert validate_input("9") == 9
    assert validate_input("9.0") == 9


def test_validate_input_type_invalid():
    assert validate_input("0") == None
    assert validate_input("a") == None
    assert validate_input("10") == None


def test_compare_num():
    assert compare_num(1, 2) == "too low"
    assert compare_num(5, 3) == "too high"
    assert compare_num(6, 6) == "exactly right"
