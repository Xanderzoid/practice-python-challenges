import pytest

from project_11.script_project_11 import validate_input


def test_validate_input():
    assert validate_input() == 0
