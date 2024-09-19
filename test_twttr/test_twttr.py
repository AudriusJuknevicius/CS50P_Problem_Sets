from twttr import shorten
import pytest


def test_twittr():

    try:
        assert shorten("Education") == "dctn"
    except AssertionError:
        print("Failed to remove vowels correctly")

    try:
        assert shorten("HELLO") == "HLL"
    except AssertionError:
        print("Failed to remove uppercase vowels")

            try:
        assert shorten("hello") == "hll"
    except AssertionError:
        print("Failed to remove lowercase vowels")

            try:
        assert shorten("H3ll0 W0rld!") == "H3ll0 W0rld!"
    except AssertionError:
        print("Failed with numbers and punctuation")

            try:
        assert shorten("rhythm") == "rhythm"
    except AssertionError:
        print("Failed with string containing no vowels")

            try:
        assert shorten("") == ""
    except AssertionError:
        print("Failed with an empty string")




