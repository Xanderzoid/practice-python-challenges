import pytest
from script_project_06 import compare_reversed_str, validate_input


def test_validate_input():
    # Test valid case 01: Valid string
    assert validate_input("racecar") == "racecar"
    # Test invalid case 02: Invalid non-string
    try:
        validate_input(12345)
    except TypeError:
        print("Test 02 passed: Integer input is invalid.")

    # Test valid case 03: Valid string
    assert validate_input("Aba ") == "aba"


def test_compare_reversed_str():
    # Test valid case 01: Valid string
    assert compare_reversed_str("racecar") == True
    # Test valid case 02: Valid string
    assert compare_reversed_str("12321") == True
    # Test valid case 03: Valid string
    assert compare_reversed_str("Truck") == False
