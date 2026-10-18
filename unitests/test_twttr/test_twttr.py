from twttr import shorten


def test_twttr():
    assert shorten("twitter") =="twttr"
def test_numbers():
    assert shorten("12345") == "12345"
def test_caps():
    assert shorten("WHATSAPP") == "WHTSPP"
def test_mixed():    
    assert shorten("W311ingt0n") == "W311ngt0n"
    

    

    