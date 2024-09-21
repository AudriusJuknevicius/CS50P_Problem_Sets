import pytest
from fuel import gauge, convert

def gauge():
    assert gauge("1") == "E"
    assert gauge("99") == "F"
    assert gauge("50") == "50%"

def convert():
    assert convert("CS50") ==
    assert convert("CS05") ==
    assert convert("CS50P") == 




