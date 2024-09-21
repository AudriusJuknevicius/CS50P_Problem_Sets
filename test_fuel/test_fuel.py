import pytest
from fuel import gauge, convert

def test_gauge():
    assert gauge(99) == "F"
    assert gauge(0) == "E"
    assert gauge(50) == "50%"
    assert gauge(1) == "E"
    assert gauge(100) == "F"


def test_convert():
    assert convert("5/10") == 50
    assert convert("1/2") == 50
    assert convert("3/4") == 75

# def test_convert_invalid():
#     assert convert("6/5") = ValueError
#     assert convert("1/0") = ZeroDivisionError


def test_convert_invalid():
    with pytest.raises(ValueError):
        convert("6/5")  # Expecting ValueError for numerator greater than denominator

    with pytest.raises(ZeroDivisionError):
        convert("1/0")  # Expecting ZeroDivisionError for division by zero
