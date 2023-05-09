from fuel import convert, gauge
import pytest


def test_correct():
    assert convert("3/4") == 75
    assert gauge(75) == "75%"

    assert convert("1/100") == 1
    assert gauge(1) == "E"

    assert convert("99/100") == 99
    assert gauge(99) == "F"


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("5/0")

def test_value_error():
    with pytest.raises(ValueError):
        convert("cat/dog")