#Given a linked list where each node has a next pointer and a random 
#pointer (which can point to any node or null), return a deep copy.
#
#head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
#Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]


class Node:
    def __init__(self, val = 0, next = None, random = None):
        self.val = val
        self.next = next
        self.random = random


def copyRandomList(head):
    if not head:
        return None

    curr = head
    while curr:
        clone = Node(curr.val)
        clone.next = curr.next
        curr.next = clone
        curr = clone.next

    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next

    curr = head
    clone_head = head.next
    while curr:
        clone = curr.next
        curr.next = clone.next
        if clone.next:
            clone.next = clone.next.next
        curr = curr.next

    return clone_head