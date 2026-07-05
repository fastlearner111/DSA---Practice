#Given head of singly linked list:
#L0 → L1 → … → Ln-1 → Ln
#Reorder to:
#L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …
#
#Input:  head = [1,2,3,4]
#Output: [1,4,2,3]
#
head = [1,2,3,4,5]
#Output: [1,5,2,4,3]

# Pattern -  Linked List
# Approach - we need to find the last element and then bring to
# the index 1 and then merge the list
# dict = two pointyer
# Big O - On, On

class ListNode:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

def reorder(head):
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    second = slow.next
    slow.next = None
    prev = None

    while second:
        temp = second.next
        second.next = prev
        prev = second
        second = temp
    
    first = head
    second = prev

    while second:
        tmp1 = first.next
        tmp2 = second.next
        first.next = second
        second.next = tmp1
        first = tmp1 
        second = tmp2

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

reorder(n1)
current = n1
while current:
    print(current.val, end = ">")
    current = current.next