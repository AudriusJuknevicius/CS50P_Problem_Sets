# import pytest
# from seasons import date2time


# def test_date2time():
# today = date.today()
# answer = str.capitalize((p.number_to_words(totaltime.days * 1440, andword="") + " minutes"))


# assert date2time("2000-12-12") == str.capitalize((p.number_to_words(.days * 1440, andword="") + " minutes"))
# assert date2time("2007-12-31") == answer


import pytest
from seasons import date2time
from datetime import date, timedelta

def test_date2time():
    today = date.today()

    # Test for a date one year ago
    one_year_ago = today - timedelta(days=365)
    expected_minutes = (today - one_year_ago).days * 24 * 60
    assert date2time(str(one_year_ago)) == f"{expected_minutes} minutes"

    # Test for a date two years ago
    two_years_ago = today - timedelta(days=730)  # 365 * 2
    expected_minutes = (today - two_years_ago).days * 24 * 60
    assert date2time(str(two_years_ago)) == f"{expected_minutes} minutes"

    # Test for today's date (should return 0 minutes)
    assert date2time(str(today)) == "0 minutes"
