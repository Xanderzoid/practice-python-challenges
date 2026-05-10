import pytest
from project_05.script_project_05 import (
    gen_num_list,
    list_intersect,
    validate_input,
)


@pytest.fixture
def sample_data_dict():
    """Sample data of random generated list of ints and their intersections."""
    num_dict = {
        "a": [1, 2, 3],
        "b": [4, 5, 6],
        "c": [1, 3, 4, 6, 9],
        "ab": [],
        "ac": [1, 3],
        "bc": [4, 6],
    }
    return num_dict


def test_gen_num_list():
    list_length = 10
    random_max = 20
    result_dict = {"max_num": False, "list_length": False}
    gen_list = gen_num_list()

    if len(gen_list) == list_length:
        result_dict["list_length"] = True
    if max(gen_list) <= random_max:
        result_dict["max_num"] = True

    assert result_dict["list_length"] and result_dict["max_num"]


def test_list_intersection(sample_data_dict):
    list_01 = list_intersect(sample_data_dict["a"], sample_data_dict["b"])
    list_02 = list_intersect(sample_data_dict["a"], sample_data_dict["c"])
    list_03 = list_intersect(sample_data_dict["b"], sample_data_dict["c"])
    ab = list_01 == sample_data_dict["ab"]
    ac = list_02 == sample_data_dict["ac"]
    bc = list_03 == sample_data_dict["bc"]

    assert ab and ac and bc


def test_validate_input(monkeypatch):
    inputs = iter(["r", "q", "25"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = validate_input()
    assert result == None
