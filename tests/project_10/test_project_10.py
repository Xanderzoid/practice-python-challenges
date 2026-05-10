import pytest
from script_project_10 import roll_dataset, merge_dataset, avg_dataset, min_max_dataset


@pytest.fixture
def sample_data_01():
    data = {f"{i}": 0 for i in range(1, 13)}
    data["1"] = 2  # 5 rolls
    data["3"] = 1
    data["6"] = 1
    data["11"] = 1
    return data


@pytest.fixture
def sample_data_02():
    data = {f"{i}": 1 for i in range(1, 13)}
    data["1"] = 2  # 12 rolls
    data["3"] = 2
    data["6"] = 0
    data["11"] = 0
    return data


@pytest.fixture
def sample_data_03():
    data = {f"{i}": 1 for i in range(1, 13)}
    return data


@pytest.fixture
def sample_data_04():
    data = {f"{i}": 2 for i in range(1, 13)}
    return data


@pytest.fixture
def sample_data_05():
    data = {f"{i}": 3 for i in range(1, 13)}
    return data


def test_roll_dataset():
    size = 10
    dice_dict = roll_dataset(size)
    for key, value in dice_dict.items():
        assert key in ["4D3", "2D6", "1D12"]
        num_of_rolls = 0
        for distro_value in value.values():
            num_of_rolls += distro_value
        assert num_of_rolls == size


def test_avg_dataset(sample_data_01):
    assert avg_dataset(sample_data_01) == 4.4


def test_min_max_dataset(sample_data_02):
    expected = {"min": [{"6": 0}, {"11": 0}], "max": [{"1": 2}, {"3": 2}]}
    actual = min_max_dataset(sample_data_02)

    # Check lengths first
    assert len(actual["min"]) == len(expected["min"])
    assert len(actual["max"]) == len(expected["max"])

    # Check contents
    for item in actual["min"]:
        assert item in expected["min"]
    for item in actual["max"]:
        assert item in expected["max"]


def test_merge_dataset(sample_data_03, sample_data_04, sample_data_05):
    data = {"data_01": sample_data_03, "data_02": sample_data_04}
    merged_data = merge_dataset(data)
    assert merged_data == sample_data_05
