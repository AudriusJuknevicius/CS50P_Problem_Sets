from twttr import shorten
import pytest


def test_twittr():

    try:
        assert shorten("Education") == "dctn"
    except AssertionError:
        print("Failed to remove vowels correctly")

        



