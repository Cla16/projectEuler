import pytest

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class Single_Linked_List:

    def __init__(self):
        self.head = None

def check_dup_2(sllist):
    has_dup = False
    front = sllist.head
    back = sllist.head
    while back is not None:
        front = back.next
        while front is not None:
            if back.data == front.data:
                has_dup = True
                break
            else:
                front = front.next
        back = back.next
    return has_dup

def test_false():
    list = Single_Linked_List()
    list.head = Node("a")
    e2 = Node("b")
    e3 = Node("c")
    list.head.next = e2
    e2.next = e3
    assert check_dup_2(list) == False

def test_true():
    list = Single_Linked_List()
    list.head = Node(1)
    e2 = Node(2)
    e3 = Node(1)
    list.head.next = e2
    e2.next = e3
    assert check_dup_2(list) == True
