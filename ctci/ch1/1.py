import pytest
def has_all_unique_characters1(string):
    """
    Take a string and determine if all characters are unique
    """
    if type(string) != str:
        return("Hey that's not a string!")
    all_unique = True
    char_count = []
    for i in range(len(string)):
        if string[i] in char_count:
            all_unique = False
        char_count.append(string[i])
    return(all_unique)

def test_unique():
    assert has_all_unique_characters1("ui") == True
def test_nonunique():
    assert has_all_unique_characters1("aa") == False
def test_invalid_input():
    assert has_all_unique_characters1(1) == "Hey that's not a string!"

def has_all_unique_characters2(string):
    """
    This time with not extra data structures
    """
    if type(string) != str:
        return("Hey that's not a string!")
    all_unique = True
    string = ''.join(sorted(string))
    for i in range(len(string) - 1):
        if string[i] == string[i+1]:
            all_unique = False
    return(all_unique)

def test_unique2():
    assert has_all_unique_characters1("ui") == True
def test_nonunique2():
    assert has_all_unique_characters2("aba") == False
def test_invalid_input2():
    assert has_all_unique_characters2(1) == "Hey that's not a string!"

