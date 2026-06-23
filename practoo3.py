#Given the head of a linked list, return true if there is a cycle,
#false otherwise. A cycle means a node's next pointer points back
#to a previous node.
#
#Input:  
head = [3,2,0,-4] #where -4 connects back to node 2
##Output: True
##
#Input:  head = [1,2], where 2 connects back to node 1
#Output: True
#
#Input:  head = [1]
#Output: False

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def isCycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next
        if slow == fast:
            return True
    return False


n1 = ListNode(3)
n2 = ListNode(2)
n3 = ListNode(0)
n4 = ListNode(-4)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n2

print(isCycle(n1))