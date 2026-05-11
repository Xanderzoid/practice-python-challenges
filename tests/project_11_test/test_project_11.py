import pytest

from project_11.script_project_11 import validate_input, is_prime, find_divisors


def test_validate_input(monkeypatch):
    inputs = iter(["1", "2", "25"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert validate_input() == 1
    assert validate_input() == 2
    assert validate_input() == 25


def test_is_prime():
    primes = [2, 3, 5, 7, 11]
    non_primes = [1, 4, 6, 8, 10, 12, 14, 15, 100]
    # Test primes
    for prime in primes:
        assert is_prime(prime) == True
    # Test non-primes
    for num in non_primes:
        assert is_prime(num) == False


def test_find_divisors():
    assert find_divisors(4) == [1, 2, 4]
    assert find_divisors(6) == [1, 2, 3, 6]
    assert find_divisors(8) == [1, 2, 4, 8]
    assert find_divisors(10) == [1, 2, 5, 10]
