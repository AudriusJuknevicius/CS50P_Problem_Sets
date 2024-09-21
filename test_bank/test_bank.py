# https://cs50.harvard.edu/python/2022/psets/5/test_bank/

import pytest
from bank import value


def test_bank():
    assert value("hello") == "$0"
    assert value("HELLO") == "$0"
    assert value("hey") == "$20"
    assert value("H3ll0 W0rld!") == "$20"
    assert value("Yo") == "$100"
    assert value("") == "$100"
