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
def sum_list(l1,l2):
    p1 = l1.head
    p2 = l2.head
    answer = SLL()
    carry = 0
    answer.head = Node((p1.data + p2.data) % 10)
    ans = answer.head
    if p1.data + p2.data >= 10:
        carry = 1
    p1 = l1.head.next
    p2 = l2.head.next
    while p1 is not None or p2 is not None or carry != 0:
        if p1 is None and p2 is not None:
            value = (p2.data + carry) % 10
            if p2.data + carry >= 10:
                carry = 1
            else:
                carry = 0
            new_node = Node(value)
            ans.next = new_node
            ans = ans.next
            p2 = p2.next
        elif p2 is None and p1 is not None:
            value = (p1.data + carry) % 10
            if p1.data + carry >= 10:
                carry = 1
            else:
                carry = 0
            new_node = Node(value)
            ans.next = new_node
            ans = ans.next
            p1 = p1.next
        elif p1 is not None and p2 is not None:
            value = (p1.data + p2.data + carry) % 10
            if p1.data + p2.data + carry >= 10:
                carry = 1
            else:
                carry = 0
            new_node = Node(value)
            ans.next = new_node
            ans = ans.next
            p1 = p1.next
            p2 = p2.next
        else:
            new_node = Node(carry)
            ans.next = new_node
            ans = ans.next
            carry = 0
    return answer
def test():
    list1 = SLL()
    list1.head = Node(7)
    n2 = Node(1)
    n3 = Node(7)
    list1.head.next = n2
    n2.next = n3
    list2 = SLL()
    list2.head = Node(5)
    n4 = Node(9)
    n5 = Node(2)
    list2.head.next = n4
    n4.next = n5
    assert sum_list(list1, list2).stringify() == "2101"

