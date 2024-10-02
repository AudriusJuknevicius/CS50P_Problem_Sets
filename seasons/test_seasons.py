import pytest
from seasons import date2time
from datetime import date, timedelta



def test_date2time():
    today = date.today()
    year = today - 365

    assert date2time(year) == "Five hundred twenty-five thousand, six hundred minutes"

