import pytest
from seasons import date2time
from datetime import date
import calendar

def test_date2time():
    today = date.today()
    yesterday = today - 1
    daybeforeyesterday = today - 2
    

