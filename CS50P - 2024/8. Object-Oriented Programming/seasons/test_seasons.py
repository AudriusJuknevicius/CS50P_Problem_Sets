import pytest
from seasons import date2time
from datetime import date, timedelta

def test_date2time():
    today = date.today()
    one_year_ago = today - timedelta(days=365)

    expected_minutes = (today - one_year_ago).days * 24 * 60
    expected_output = f"{expected_minutes} minutes"

    assert date2time(str(one_year_ago)) == "Five hundred twenty-five thousand, six hundred minutes"
