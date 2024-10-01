import pytest
from um import count

def test_count():
    assert count("hello, um, world") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("yummy") == None
    assert count("um, thanks, um....") == 2
