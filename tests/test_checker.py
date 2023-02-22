import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from python.main import PrimeNumberChecker
import pytest

# test for prime
def test_is_prime():
    assert PrimeNumberChecker(1,10).is_prime() == [2, 3, 5, 7]

# test for twin prime
def test_is_twin_prime():
    assert PrimeNumberChecker(1,10).is_twin_prime() == [[3, 5], [5, 7]]

# This exception is moved to app.py
"""
def test_value_error():

    with pytest.raises(ValueError) as e:
        PrimeNumberChecker(99,10).is_prime()

    assert str(e.value) == "The input maximum value has to be larger than the input minimum value."
"""