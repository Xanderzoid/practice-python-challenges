import pytest
from project_14.script_project_14 import validate_input, gen_dup_list, remove_dup


def test_validate_input_valid():
    assert validate_input(" Y ") == "y"
    assert validate_input("yes") == "y"
    assert validate_input("") == "y"
    assert validate_input("q") == "q"
    assert validate_input("quit") == "q"


def test_validate_input_invalid():
    with pytest.raises(ValueError):
        validate_input("abc")
    with pytest.raises(ValueError):
        validate_input("123")


def test_gen_dup_list():
    length, num_dup = 10, 3
    dup_list = gen_dup_list(length, num_dup)
    dup_size = len(dup_list)
    assert dup_size == length + num_dup
    assert len(list(set(dup_list))) < dup_size


def test_remove_dup():
    dup_list = [0, 1, 2, 2, 3, 4, 5, 5]
    cleaned_list = remove_dup(dup_list)
    assert len(set(cleaned_list)) == len(cleaned_list)
