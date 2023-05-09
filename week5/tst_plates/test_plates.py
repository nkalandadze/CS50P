# დავალება #30 - Re-requesting a Vanity Plate
from plates import is_valid


def test_len():
    assert is_valid("n") == False
    assert is_valid("ni") == True
    assert is_valid("kalandadze") == False

def test_beginning():
    assert is_valid("N5") == False
    assert is_valid("55") == False

def test_first_digit():
    assert is_valid("cs505") == True
    assert is_valid("cs050") == False

def test_middle_numbers():
    assert is_valid("ni5ni") == False

def test_alphanumeric():
    assert is_valid("ni.ni") == False