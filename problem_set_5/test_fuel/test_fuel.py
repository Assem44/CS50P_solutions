from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("3/4") == 75
    assert convert("4/4") == 100
    assert convert("1/4") == 25
    assert convert("0/4") == 0

def test_convert_errors():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("three/four")
    with pytest.raises(ValueError):
        convert("-1/3")
    with pytest.raises(ValueError):
        convert("5/4")
    with pytest.raises(ValueError):
        convert("1.5/3")

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(85) == "85%"
