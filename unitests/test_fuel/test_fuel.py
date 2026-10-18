from fuel import convert, gauge, main

def test_convert():
    assert convert("1/2") == 50.0

def test_zero_div():
    assert convert("1/0") == None

def test_neg():
    assert convert("-1/1") == -100

def letters():
    assert gauge(100) == "F"
    assert gauge(0) == "E"

