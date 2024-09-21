import pytest
from fuel import gauge, convert

def gauge():
    assert gauge("0/1") == "E"
    assert gauge("99") == "F"
    assert gauge("5/10") == "50%"

def convert():
    assert convert("CS50") == ValueError
    assert convert("0") == ZeroDivisionError




