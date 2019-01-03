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
 
def reverse(llist):
    new_list = SLL()
    p = llist.head
    while p is not None:
        if new_list.head is None:
            new_node = Node(p.data)
            new_list.head = new_node
            p = p.next
        else:
            new_node = Node(p.data)
            new_node.next = new_list.head
            new_list.head = new_node
            p = p.next
    return new_list

def is_pal(llist):
    rev = reverse(llist)
    p1 = llist.head
    p2 = rev.head
    is_pal = True
    while p1 is not None:
       if p1.data != p2.data:
           is_pal = False
           break
       p1 = p1.next
       p2 = p2.next
    return is_pal

def testpal():
    l = SLL()
    l.head = Node(1)
    n2 = Node(2)
    n3 = Node(1)
    l.head.next = n2
    n2.next = n3
    assert is_pal(l) == True

def testnopal():
    l = SLL()
    l.head = Node(1)
    n2 = Node(2)
    l.head.next = n2
    print(l.stringify())
    print(reverse(l).stringify())
    assert is_pal(l) == False
