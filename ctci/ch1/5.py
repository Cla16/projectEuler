import pytest 

def one_away(a,b):
    if type(a) != str or type(b) != str:
        return False
    if abs(len(a) - len(b)) > 1:
        return False
    is_one_away = True
    edits = 0
    if len(a) == len(b):
        for i in range(len(a)):
            if a[i] != b[i]:
                edits += 1
            if edits > 1:
                is_one_away = False
                break
    else:
        if len(a) > len(b):
           short = b
           large = a
        else:
            short = a
            large = b
        i = 0
        j = 0
        while i < len(short) and j < len(large):
           if short[i] != large[j]:
                j += 1
                edits += 1
           else:
                i += 1
                j += 1
           if edits > 1:
               is_one_away = False
               break
    return is_one_away
def test1():
    assert one_away("pale", "ple") == True
def test2():
    assert one_away("pales", "pale") == True
def test3():
    assert one_away("pale", "bale") == True
def test4():
    assert one_away("pale", "bake") == False
def test_invalid():
    assert one_away("pale", 1) == False
    
