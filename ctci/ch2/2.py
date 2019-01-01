import pytest

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:

    def __init__(self):
        self.head = None

def k_to_last(sllist, k):
    back = sllist.head
    front = sllist.head
    for i in range(k):
        front = front.next
    while front is not None:
        back = back.next
        front = front.next
    return back.data

def test1():
    list = SLL()
    list.head = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    list.head.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    assert k_to_last(list, 2) == 4


