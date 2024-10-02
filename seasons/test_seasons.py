import pytest
from seasons import date2time
from datetime import date, timedelta

def test_date2time():
    today = date.today()
    assert date2time(today.day - 365) == 365
    # assert count("Um, thanks for the album.") == 1
    # assert count("yummy") == 0
    # assert count("um, thanks, um....") == 2
