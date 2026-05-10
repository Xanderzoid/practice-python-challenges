import pytest
from project_07.script_project_07 import extract_even


def test_extract_even():
    # Test valid list 01: valid list
    list_01 = [0, 21, 2, 76]
    assert extract_even(list_01) == [0, 2, 76]
    # Test invalid list 02: empty list
    list_02 = []
    try:
        extract_even(list_02)
    except ValueError:
        print("Test 02 passed: raised ValueError on empty list.")

    # Test invalid list 03: str list
    list_03 = ["string", 1, 64]
    try:
        extract_even(list_03)
    except TypeError:
        print("Test 03 passed: rasied TypeError on string list.")

    # Test valid list 04: duplicate numbers
    list_04 = [2, 56, 56, 9]
    assert extract_even(list_04) == [2, 56]
