import pytest

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    
    def __init__(self):
        self.head = None
    
    def stringify(self):
        printdata = self.head
        string = ""
        while printdata is not None:
            string += printdata.data
            printdata = printdata.next
        return string
def del_node(n):
    nex = n.next
    n.data = nex.data
    n.next = nex.next

def test(): #need a better written test here, right now just evaluate stdout
    list = SLL()
    list.head = Node("a")
    n2 = Node("b")
    n3 = Node("c")
    list.head.next = n2
    n2.next = n3
    del_node(n2)
    assert list.stringify() == "ac"
