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
    # Use a known date (e.g., today's date) and subtract a fixed number of days
    today = date.today()
    two_days_ago = today - timedelta(days=2)

    # Test if the function returns the correct result for 2 days ago
    assert "two thousand eight hundred eighty minutes" in date2time(str(two_days_ago))

    # Another test case, e.g., 1 day ago
    one_day_ago = today - timedelta(days=1)
    assert "one thousand four hundred forty minutes" in date2time(str(one_day_ago))
