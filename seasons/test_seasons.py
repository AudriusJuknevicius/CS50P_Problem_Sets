import pytest
from seasons import date2time
from datetime import date

def test_date2time():
    # Define a known reference date (e.g., a year ago from today)
    today = date.today()
    one_year_ago = today.replace(year=today.year - 1)
    two_years_ago = today.replace(year=today.year - 2)

    # Test cases for known differences
    assert "Five hundred twenty-five thousand six hundred minutes" in date2time(str(one_year_ago))  # 1 year in minutes
    assert "One million fifty-one thousand two hundred minutes" in date2time(str(two_years_ago))   # 2 years in minutes
