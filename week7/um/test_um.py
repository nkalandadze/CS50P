from um import count

def test_in_word():
    assert count("album") == 0

def test_upper_or_lower():
    assert count("UM") == 1
    assert count("um") == 1
    assert count("Um") == 1
    assert count("uM") == 1

def test_with_whitespace():
    assert count(" um ") == 1

def test_big_string():
    assert count("Um, thanks for the album") == 1
    assert count("um?") == 1
    assert count("Um, thanks, um...") == 2