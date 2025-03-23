import pytest
from plates import is_valid

def test_plates():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False
    assert is_valid("P13.14") == False
    assert is_valid("H") == False
    assert is_valid("") == False
    assert is_valid("CS") == True
    assert is_valid("CS50!") == False
    assert is_valid("CS 50") == False
    assert is_valid("123ABC") == False
    assert is_valid("A123BC") == False
    assert is_valid("22") == False


