import pytest
from plates import is_valid

def test_plates():
    assert is_valid("hello") == 0
    assert is_valid("HELLO") == 0
    assert is_valid("hey") == 20
    assert is_valid("H3ll0 W0rld!") == 20
    assert is_valid("Yo") == 100
    assert is_valid("") == 100

