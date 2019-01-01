import pytest

def compress(a):
    if type(a) != str:
        return False
    compressed = ""
    count = 1
    for i in range(len(a)):
        if i >= len(a) - 1 or a[i] != a[i + 1]:
            compressed = compressed + a[i] + str(count)
            count = 1
        elif a[i] == a[i+1]:
            count += 1
    if a[-1] != a[-2]:
        compressed = compressed + a[-1] + "1"
    if len(compressed) < len(a):
        return compressed
    else:
        return a

def test1():
    assert compress("aabcccccaaa") == "a2b1c5a3"
def test2():
    assert compress("abcde") == "abcde"
def test3():
    assert compress("aaaaavvvvddddsss") == "a5v4d4s3"
def test_invalid_input():
    assert compress(1) == False
