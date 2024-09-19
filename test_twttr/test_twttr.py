from twttr import shorten

def test_twittr():
    assert shorten("Education") == "dctn"
    assert shorten("HELLO") == "HLL"
    assert shorten("hello") == "hll"
    assert shorten("H3ll0 W0rld!") == "H3ll0 W0rld!"
    assert shorten("rhythm") == "rhythm"
    assert shorten("") == ""
