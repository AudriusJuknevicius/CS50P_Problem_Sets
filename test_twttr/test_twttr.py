from twttr import shorten
import pytest

def main():
    test_twittr()


def test_twittr():

    try:
        assert shorten("Education") == "dctn"
    except AssertionError:
        print("The result did not ommit all vowels")



if __name__ == "__main__":
    main()
