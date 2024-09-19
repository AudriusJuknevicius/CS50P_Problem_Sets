from twttr import shorten

def main():
    test_twittr()


def test_twittr():

    try:
        assert shorten("A") == ""
    except AssertionError:
        print("Vowel A was not ommited")

    try:
        assert shorten("a") == ""
    except AssertionError:
        print("Vowel a was not ommited")

        



if __name__ == "__main__":
    main()
