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

    # Test for 2 days ago
    two_days_ago = today - timedelta(days=2)
    expected_minutes = 2 * 24 * 60  # 2 days in minutes
    assert date2time(str(two_days_ago)) == f"{expected_minutes} minutes"

    # Test for 1 day ago
    one_day_ago = today - timedelta(days=1)
    expected_minutes = 1 * 24 * 60  # 1 day in minutes
    assert date2time(str(one_day_ago)) == f"{expected_minutes} minutes"

    # Test for today's date (should return 0 minutes)
    assert date2time(str(today)) == "0 minutes"
