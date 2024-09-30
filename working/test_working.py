import pytest
from working import convert

def test_convert():
    assert test_convert("001.001.001.001") == True
    assert test_convert("0.0.0.0") == True
    assert test_convert("255.255.255.255") == True
    assert test_convert("256.255.255.255") == False
    assert test_convert("255.255.255.256") == False
    assert test_convert("") == False
    assert test_convert("?.?.?.?") == False
    assert test_convert("...") == False
