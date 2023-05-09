from numb3rs import validate

def test_numbers():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("512.512.512.512") == False
    assert validate("1.1.1.1000") == False
    assert validate("1.1.1") == False

def test_characters():
    assert validate("cat") == False