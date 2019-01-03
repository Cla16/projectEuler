import pytest

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:

    def __init__(self):
        self.head = None
    
    def stringify(self):
        data = self.head
        string = ""
        while data is not None:
            string += str(data.data)
            data = data.next
        return string
     
    def length(self):
        data = self.head
        counter = 0
        while data is not None:
            counter += 1
            data = data.next
        return counter

def cross_list(l1, l2):
    if l1.length() > l2.length():
        for i in range(l1.length() - l2.length()):
            new_node = Node(0)
            new_node.next = l2.head
            l2.head = new_node
    elif l2.length() > l1.length():
        for i in range(l2.length() - l1.length()):
            new_node = Node(0)
            new_node.next = l1.head
            l1.head = new_node
    p1 = l1.head
    p2 = l2.head
    has_cross = False
    while p1 is not None:
        if p1 == p2:
            has_cross = True
            break
        else:
            p1 = p1.next
            p2 = p2.next
    return has_cross

def testcross():
    l1 = SLL()
    l2 = SLL()
    l1.head = Node(2)
    n2 = Node(3)
    n3 = Node(4)
    n4 = Node(1)
    l2.head = Node(3)
    n22 = Node(4)
    n24 = Node(6)
    l1.head.next = n2
    n2.next = n3
    n3.next = n4
    l2.head.next = n22
    n22.next = n3
    assert cross_list(l1, l2) == True

def testnocross():
    l1 = SLL()
    l2 = SLL()
    l1.head = Node(2)
    n2 = Node(3)
    n3 = Node(4)
    n4 = Node(1)
    l2.head = Node(3)
    n22 = Node(4)
    n24 = Node(6)
    l1.head.next = n2
    n2.next = n3
    n3.next = n4
    l2.head.next = n22
    n22.next = n24
    assert cross_list(l1, l2) == False


