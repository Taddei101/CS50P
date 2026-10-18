from bank import value

def test_value():
    assert value("hello") == "$0"    

def test_hi():
    assert value("hi") == "$20"

def test_whazup():
    assert value("Whazup") == "$100"