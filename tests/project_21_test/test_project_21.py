import pytest
from project_21.script_project_21 import sanitize_input, validate_input, has_filepath, write_to_file, quit_or_continue, find_new_filename

# Global Constants
FILEPATH = "./data/test.txt"

@pytest.mark.parametrize("raw, expected", [(" 1 ", "1"), ("\t2\n", "2"), (" 3  ", "3"), ("abc", "abc")])
def test_sanitize_input(raw, expected):
    assert sanitize_input(raw) == expected

@pytest.mark.parametrize("user_input, expected", [
    ('yes', True),
    ('y', True),
    ('no', True),
    ('n', True),
    ('', False),
    ("quit", True),
    ("q", True),
    ("exit", True),
    ("q0", False),
    ("123", False),
])
def test_validate_input(user_input, expected):
    assert validate_input(user_input) == expected

def test_has_filepath():
    assert has_filepath(FILEPATH) == False

def test_write_to_file():
    # If test.txt does exist
    assert write_to_file("test.txt", FILEPATH) == False
    
def test_quit_or_continue():
    assert quit_or_continue("q") == "q"
    assert quit_or_continue("y") == "y"
    assert quit_or_continue("b") == "invalid"

def test_find_new_filename():
    assert find_new_filename("./data/test") == "./data/test_1.txt"
