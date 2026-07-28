
class Node:
    def __init__(self, val = 0, next = None, random = None):
        self.val = val
        self.next = next
        self.random = random

def copy(head):
    if not head:
        return None

    curr = head
    while curr:
        clone = Node(curr.val)
        clone.next = curr.next
        curr.next = clone
        curr = clone.next
        