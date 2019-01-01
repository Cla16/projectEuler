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

list = Single_Linked_List()
list.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

list.head.next = e2

e2.next = e3

list.listprint()
