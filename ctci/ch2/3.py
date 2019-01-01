import pytest

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    
    def __init__(self):
        self.head = None
    
    def printlist(self):
        printdata = self.head
        while printdata is not None:
            print(printdata.data)
            printdata = printdata.next
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
    assert list.printlist() == "a c"
