import pytest 
from project_22.file_io import find_file, read_from_file, clean_data
from project_22.script_project_22 import sanitize_input, validate_input
from pathlib import Path

@pytest.mark.parametrize("raw, expected", [(" 1 ", "1"), ("\t2\n", "2"), (" 3  ", "3"), ("abc", "abc")])
def test_sanitize_input(raw, expected):
    assert sanitize_input(raw) == expected

@pytest.mark.parametrize("user_input, expected", [
    ("y", "y"),
    ("yes", "y"),
    ("n", "q"),
    ("no", "q"),
    ("", "y"),
    ("q", "q"),
    ("quit", "q"),
    ("123", "invalid"),
])
def test_validate_input(user_input, expected):
    assert validate_input(user_input) == expected

def test_find_file(tmp_path):
    # Define isolated directory
    file_path = tmp_path / "test_file.txt"

    # Test file does not exist
    assert find_file(str(file_path)) is False

    # Create a temp file on disk 
    file_path.write_text("Hello World", encoding="utf-8")
    
    # Test file exists
    assert find_file(str(file_path)) is True

def test_read_from_file(tmp_path):
    # Define isolated directory
    file_path = tmp_path / "test_file.txt"

    # Test file does not exist
    assert read_from_file(str(file_path)) == []

    # Create a temp file on disk 
    file_path.write_text("Hello World", encoding="utf-8")
    
    # Test file exists
    assert read_from_file(str(file_path)) == ["Hello World"]

def test_clean_data():
    data = ["\nHello\n", "World\n"]
    assert clean_data(data) == ["Hello", "World"]
