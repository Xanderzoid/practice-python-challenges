import pytest
from script_project_08 import get_hand, generate_hand, game_logic, hand_dict


def test_hand_dict():
    assert hand_dict("r") == {"r": True, "p": False, "s": False}
    assert hand_dict("p") == {"r": False, "p": True, "s": False}
    assert hand_dict("s") == {"r": False, "p": False, "s": True}


def test_generate_hand():
    for _ in range(5):
        assert generate_hand() in "rps"


def test_game_logic():
    hands = [
        {"r": True, "p": False, "s": False},
        {"r": False, "p": True, "s": False},
        {"r": False, "p": False, "s": True},
    ]
    assert game_logic(hands[0], hands[1]) == {"player": False, "computer": True}
    assert game_logic(hands[0], hands[2]) == {"player": True, "computer": False}
    assert game_logic(hands[1], hands[2]) == {"player": False, "computer": True}
    # Tie
    assert game_logic(hands[0], hands[0]) == {"player": True, "computer": True}
    assert game_logic(hands[1], hands[1]) == {"player": True, "computer": True}
    assert game_logic(hands[2], hands[2]) == {"player": True, "computer": True}


def test_get_hand_type_valid():
    assert get_hand("r") == "r"
    assert get_hand(" R ") == "r"


def test_get_hand_type_invalid():
    with pytest.raises(ValueError):
        get_hand("abc")
