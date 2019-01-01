import pytest

class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None

class Single_Linked_List:

    def __init__(self):
        self.head = None

    def listprint(self):
        printdata = self.head
        while printdata is not None:
            print(printdata.data)
            printdata = printdata.next

def check_dup(sllist):
    char = []
    has_dup = False
    n = sllist.head
    while n is not None:
        if n.data in char:
            has_dup = True
            break
        char.append(n.data)
        n = n.next
    return has_dup

def test_false():
    list = Single_Linked_List()
    list.head = Node("Mon")
    e2 = Node("Tue")
    e3 = Node("Wed")
    list.head.next = e2
    e2.next = e3
    assert check_dup(list) == False

def test_true():
    list = Single_Linked_List()
    list.head = Node(1)
    e2 = Node(2)
    e3 = Node(1)
    e4 = Node(6)
    list.head.next = e2
    e2.next = e3
    e3.next = e4
    assert check_dup(list) == True
