import pytest
from seasons import date2time
from datetime import date
import calendar

def test_date2time():
    today = date.today()

    # Define the date one and two years ago
    one_year_ago = today.replace(year=today.year - 1)
    two_years_ago = today.replace(year=today.year - 2)

    # Calculate expected minutes (accounting for leap year)
    one_year_minutes = 525_600  # Regular year
    two_years_minutes = 2 * 525_600  # Regular two years

    # Check if any of the years crossed are leap years
    if calendar.isleap(one_year_ago.year):
        one_year_minutes += 1_440  # Extra day in leap year

    if calendar.isleap(one_year_ago.year) or calendar.isleap(two_years_ago.year):
        two_years_minutes += 1_440  # One extra day if either year was a leap year

    # Test cases for known differences
    assert str(one_year_minutes) in date2time(str(one_year_ago))  # 1 year in minutes
    assert str(two_years_minutes) in date2time(str(two_years_ago))  # 2 years in minutes
