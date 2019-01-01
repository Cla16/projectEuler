import pytest

def pal_perm(string):
    if type(string) != str:
        return False
    if len(string) == 0 or len(string) == 1:
        return True
    dict = {}
    odd_count = 0
    is_perm = True
    for i in range(len(string)):
        if string[i] not in dict and string[i] != " ":
            dict[string[i]] = 1
        elif string[i] != " ":
            dict[string[i]] += 1
    for keys in dict:
        if dict[keys] % 2 == 1:
            odd_count += 1
    if odd_count > 1:
        is_perm = False
    return(is_perm)

def test_pal():
    assert pal_perm("taco cat") == True
def test_perm():
    assert pal_perm("car race") == True
def test_empty():
    assert pal_perm("") == True
def test_false():
    assert pal_perm("monkey") == False
def test_invalid_input():
    assert pal_perm(1) == False
