# დავალება #29 - Back to the Bank
from bank import value

def test_hello():
    assert value("Hello") == 0
    assert value(" Hello") == 0
    assert value("hello") == 0

def test_h():
    assert value("h") == 20
    assert value("hi") == 20
    assert value("HI") == 20
    assert value("  how are you") == 20

def test_other():
    assert value("what's up?") == 100
    assert value("gamarjoba") == 100

