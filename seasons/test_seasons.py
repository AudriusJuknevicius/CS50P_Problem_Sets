import pytest
from seasons import date2time
from datetime import date, timedelta

def test_date2time():
    today = date.today()

    # Define dates like yesterday and the day before yesterday
    yesterday = today - timedelta(days=1)
    day_before_yesterday = today - timedelta(days=2)

    # Calculate expected minute values for the differences
    one_day_in_minutes = 1 * 1440  # 1 day in minutes
    two_days_in_minutes = 2 * 1440  # 2 days in minutes

    # Test cases for known differences
    assert str(one_day_in_minutes) in date2time(str(yesterday))  # 1 day in minutes
    assert str(two_days_in_minutes) in date2time(str(day_before_yesterday))  # 2 days in minutes
