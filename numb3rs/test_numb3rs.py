import pytest
from numb3rs import validate

def test_numb3rs():
    assert validate("001.001.001.001") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("256.255.255.255") == False
    assert validate("255.255.255.256") == False
    assert validate("") == False
    assert validate("?.?.?.?") == False
    assert validate("...") == False
