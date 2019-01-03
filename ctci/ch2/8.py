import pytest

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:

    def __init__(self):
        self.head = None
    
def loop(slist):
    slow = slist.head.next
    fast = slist.head.next.next
    while slow != fast:
        if slow is None or fast is None:
            return False
        fast = fast.next.next
        slow = slow.next
    slow = slist.head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return fast

def testloop():
    l = SLL()
    l.head = Node(1)
    n2 = Node(2)
    nloop = Node(3)
    n3 = Node(4)
    n4 = Node(5)
    l.head.next = n2
    n2.next = nloop
    nloop.next = n3
    n3.next = n4
    n4.next = nloop
    assert loop(l) == nloop
