#Given the head of a singly linked list, reverse the list and return the new head.
head = [1, 2, 3, 4, 5]
#Output: [5, 4, 3, 2, 1]
#
#Input:  head = [1, 2]
#Output: [2, 1]
#
#Input:  head = []
#Output: []

# so first we crete a class
# then init function
# then we create the main fucntion, the main code goes
# the variables we need are prev, curr,
# then create a test fucntion,
# then call the function
# then the main loop

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
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

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next= n5

head = isreverse(n1)

current = head
while current:
    print(current.val, end = ">")
    current = current.next