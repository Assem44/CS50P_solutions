from plates import is_valid

def test_length():
    assert is_valid("ab") == True
    assert is_valid("abcdef") == True
    assert is_valid("a") == False
    assert  is_valid("abcdefg") == False

def test_starts_with_alpha():
    assert is_valid("aa") == True
    assert is_valid("11") == False
    assert is_valid("1a") == False
    assert is_valid("a1") == False

def test_numbers():
    assert is_valid("abcd12") == True
    assert is_valid("aaa012") == False
    assert is_valid("ab12cd") == False
    assert is_valid("abc12g") == False

def test_punctuation():
    assert is_valid("aa.3") == False
    assert is_valid("aa 34") == False
    assert is_valid("aa$34") == False
