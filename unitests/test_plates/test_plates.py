from plates import is_valid

def test_plates1():
    assert is_valid("BB11") == True

def test_plates2():
    assert is_valid("11BBB") == False