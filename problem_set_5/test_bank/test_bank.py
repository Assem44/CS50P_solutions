from bank import value

def test_zero():
    assert value("hello, man") == 0
    assert value("Hello, man") == 0
    assert value("HELLO, MAN") == 0

def test_twenty():
    assert value("hi") == 20
    assert value("Hey") == 20
    assert value("HOW YOU DOING?") == 20

def test_hundred():
    assert value("word") == 100
    assert value("GOOD MORNING") == 100
    assert value("123@") == 100

