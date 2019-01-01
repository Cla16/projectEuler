import pytest

def urlify(string):
    if type(string) != str:
        return False
    url_string = ""
    for i in range(len(string)):
        if string[i] != " ":
            url_string += string[i]
        else:
            url_string += "%20"
    return(url_string)

def test_string():
    assert urlify("Mr John Smith") == "Mr%20John%20Smith"
def test_invalid_input():
    assert urlify(1) == False
