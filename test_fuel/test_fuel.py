import pytest
from fuel import gauge, convert

def gauge():
    assert gauge("CS50") == True
    assert gauge("CS05") == False
    assert gauge("CS50P") == False

def convert():
    assert convert("CS50") == True
    assert convert("CS05") == False
    assert convert("CS50P") == False




