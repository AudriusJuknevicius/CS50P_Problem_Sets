import pytest
from seasons import date2time

def test_date2time():
    assert date2time("hello, um, world") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("yummy") == 0
    assert count("um, thanks, um....") == 2
