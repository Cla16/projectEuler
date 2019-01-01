import pytest

def is_permutation(a, b):
    permutation = True
    if type(a) != str or type(b) != str:
        return False
    if len(a) != len(b):
       return False
    a_dict = {}
    b_dict = {}
    for i in range(len(a)):
        if a[i] not in a_dict:
            a_dict[a[i]] = 1
        else:
            a_dict[a[i]] += 1
        if b[i] not in b_dict:
            b_dict[b[i]] = 1
        else:
            b_dict[b[i]] += 1
    if a_dict != b_dict:
        permutation = False
    return permutation

def test_permutation():
    assert is_permutation("abba", "baba") == True
def test_noperm():
    assert is_permutation("abba", "cbba") == False
def test_invalid_input():
    assert is_permutation(1, "blah") == False
