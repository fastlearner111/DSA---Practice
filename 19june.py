#Given the head of a singly linked list, reverse the list
#and return the reversed list's head.

head = [1,2,3,4,5]
#Output: [5,4,3,2,1]
#
#Input:  head = [1,2]
#Output: [2,1]
#
#Input:  head = []
#Output: []

class LinkedNode:
    def __init__(self, val = 0, next = None):
        self. val = val
        self.next = next

def isreverse(head):
    prev = None
    curr = head

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

n1 = LinkedNode(1)
n2 = LinkedNode(2)
n3 = LinkedNode(3)
n4 = LinkedNode(4)
n5 = LinkedNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

head = isreverse(n1)

current = head
while current:
    print(current.val, end = ">")
    current = current.next
    