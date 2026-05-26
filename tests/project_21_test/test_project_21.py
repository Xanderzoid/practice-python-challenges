import pytest
from pathlib import Path
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
    ('', True),
    ("quit", True),
    ("q", True),
    ("exit", True),
    ("q0", False),
    ("123", False),
])
def test_validate_input(user_input, expected):
    assert validate_input(user_input) == expected

def test_quit_or_continue():
    assert quit_or_continue("q") == "q"
    assert quit_or_continue("y") == "y"
    assert quit_or_continue("b") == "invalid"

def test_hask_filepath(tmp_path):
    # Defnie a isolated directory
    test_file = tmp_path / "test.txt"

    # Test file does not exist
    assert has_filepath(str(test_file)) is False

    # Create a temp file on disk 
    test_file.write_text("Hello World", encoding="utf-8")
    
    # Test file exists
    assert has_filepath(str(test_file)) is True

def test_write_to_file(tmp_path):
    # Setup destination path in temp directory
    target_destination = tmp_path / "output_test.txt"
    sample_quotes = ["Quote 1", "Quote 2", "Quote 3"]

    result = write_to_file(sample_quotes, str(target_destination))

    assert result is True
    assert target_destination.exists() is True

    # Verify file content
    with open(target_destination, "r", encoding="utf-8") as file:
        assert file.read() == "Quote 1\nQuote 2\nQuote 3\n"

def test_write_to_file_false(tmp_path):
    # Setup destination path in temp directory
    target_destination = tmp_path / "non_existent_folder" / "output_test.txt"
    sample_quotes = ["Quote 1", "Quote 2", "Quote 3"]

    result = write_to_file(sample_quotes, str(target_destination))

    assert result is False

def test_find_new_filename(tmp_path):
    # base filepath
    base_filepath = tmp_path / "test"
    # Expected filepaths
    expected_first_filepath = tmp_path / "test_1.txt"
    expected_second_filepath = tmp_path / "test_2.txt"
    
    assert find_new_filename(str(base_filepath)) == str(expected_first_filepath)
    # Create a temp file on disk
    expected_first_filepath.write_text("Hello World", encoding="utf-8")
    assert find_new_filename(str(base_filepath)) == str(expected_second_filepath)
