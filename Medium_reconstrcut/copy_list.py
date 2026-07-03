#Given a linked list where each node has a next pointer and a random 
#pointer (which can point to any node or null), return a deep copy.
#
#head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
#Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

#Pattern - Linked List
# Data Strcuture - dict
# Approach - so we need the input and output to be the same
# so we 
# Big O - On, O1

class ListNode:
    def __init__(self, val = None, next = None, random = None):
        self.val = val
        self.next = next

def copy(head):
    old_to_new = {None:None}

    curr = head
    while curr:
        old_to_new[curr] = ListNode(curr.val)
        curr = curr.next

    curr = head 
    while curr:
        old_to_new[curr].next = old_to_new[curr.next]
        old_to_new[curr].random = old_to_new[curr.random]
        curr = curr.next

    return old_to_new[head]

n1 = ListNode(7)
n2 = ListNode(13)
n3 = ListNode(11)
n4 = ListNode(10)
n5 = ListNode(1)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n1.random = None
n2.random = n1
n3.random = n5
n4.random = n3
n5.random = n1

result = copy(n1)
current = result
while current:
    print(current.val, end = ">")
    current = current.next
