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
            string += str(data.data) + ", "
            data = data.next
        return string
def partition(sllist, n):
    new_list = SLL()
    p = sllist.head
    while p is not None:
        if new_list.head is None:
            new_list.head = Node(p.data)
            tail = new_list.head
            first = new_list.head.data
            p = p.next
        
        if p.data < n:
            new_node = Node(p.data)
            new_node.next = new_list.head
            new_list.head = new_node
        elif p.data > n:
            new_node = Node(p.data)
            tail.next = new_node
            tail = new_node
        if first >= n:
            if p.data == n:
                new_node = Node(p.data)
                new_node.next = new_list.head
                new_list.head = new_node
        elif first < n:
            if p.data == n:
                new_node = Node(p.data)
                tail.next = new_node
                tail = new_node
        p = p.next
    return new_list

def test1():
    list = SLL()
    list.head = Node(3)
    n2 = Node(5)
    n3 = Node(8)
    n4 = Node(5)
    n5 = Node(10)
    n6 = Node(2)
    n7 = Node(1)
    list.head.next = n2 
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7
    print(list)
    assert partition(list, 5).stringify() == "1, 2, 3, 5, 8, 5, 10, " 

