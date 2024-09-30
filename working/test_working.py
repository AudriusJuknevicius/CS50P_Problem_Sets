import pytest
from working import convert

def test_convert():
    assert test_convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert test_convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert test_convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert test_convert("9 AM to 5:00 PM") == "09:00 to 17:00"
    assert test_convert("12:00 AM to 1:00 AM") == "00:00 to 01:00"
    assert test_convert("12 AM to 1 AM") == "00:00 to 01:00"
    assert test_convert("12:00 PM to 1:00 PM") == "12:00 to 13:00"
    assert test_convert("12 PM to 1 PM") == "12:00 to 13:00"
    with pytest.raises(ValueError): test_convert("9:60 AM to 5:00 PM")
    with pytest.raises(ValueError): test_convert("9:00 AM to 5:60 PM")
