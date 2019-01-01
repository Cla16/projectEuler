import pytest

def strotate(a,b):
    if type(a) != str or type(b) != str:
        return False
    if len(a) != len(b):
        return False
    # Clever solution here is to just double a
    a = a + a
    if b in a:
        return True
    else:
        return False

def test1():
    assert strotate("water", "rwate") == True
def test2():
    assert strotate("water", "etwar") == False
def test3():
    assert strotate("Hi", 1) == False
