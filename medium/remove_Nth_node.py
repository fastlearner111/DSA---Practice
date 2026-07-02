#Given the head of a linked list, remove the nth node from the end 
#and return the head.
#
head = [1,2,3,4,5]
n = 2
#Output: [1,2,3,5]
#
#Input:  head = [1], n = 1
#Output: []
#
#Input:  head = [1,2], n = 1
#Output: [1]

 # we need to find the element we want to remove
 # then we will remove the element 
 # then we merge the remaining


class ListNode:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

def removal(head, n):
    dummy = ListNode(0)
    dummy.next = head
    slow = dummy
    fast = dummy

   
    for i in range(n + 1):
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next
    
    slow.next = slow.next.next

    return dummy.next

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

head = removal(n1, 2)
current = head
while current:
    print(current.val, end = ">")
    current = current. next
