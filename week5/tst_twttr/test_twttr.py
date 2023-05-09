# დავალება #28 - Testing my twittr
from twttr import shorten

def test_lower():
    assert shorten("nini") == "nn"
    assert shorten("hello") == "hll"
    assert shorten("sc50!") == "sc50!"

def test_upper():
    assert shorten("NINI") == "NN"
    assert shorten("HELLO") == "HLL"
    assert shorten("SC50!") == "SC50!"