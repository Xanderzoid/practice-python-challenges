import pytest
from script_project_03 import (
    display_result,
    validate_input,
    compute_list,
)


@pytest.fixture
def sample_data():
    """Sample data of a list of user inputs, number list, and excepted list."""
    user_num_list = [1, 5, 2, 25]
    num_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    expected_list = [[], [1, 1, 2, 3], [1, 1], [1, 1, 2, 3, 5, 8, 13, 21]]
    return [user_num_list, num_list, expected_list]


def test_validate_input(monkeypatch):
    inputs = iter(["abc", "1", "25"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = validate_input()
    assert result == 1


def test_display_results(sample_data):
    user_num_list, num_list, expected_list = sample_data

    result_bool_list = []
    for user_num in user_num_list:
        result = display_result(user_num, num_list)
        if "List of numbers less than" in result:
            result_bool_list.append(True)
        else:
            result_bool_list.append(False)

    expected_bool_list = [True if len(x) > 0 else False for x in expected_list]
    assert result_bool_list == expected_bool_list


def test_compute_list(sample_data):
    user_num_list, num_list, expected_list = sample_data

    result_list = []
    for user_num in user_num_list:
        result = compute_list(user_num, num_list)
        result_list.append(result)
    assert result_list == expected_list
