#Given the head of a linked list, return true if there is a cycle,
#false otherwise.

head = [3,2,0,-4]#, where -4 connects back to node 2
#Output: True
#
#Input:  head = [1]
#Output: False

class LinkedList:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def listcycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

n1 = LinkedList(3)
n2 = LinkedList(2)
n3 = LinkedList(0)
n4 = LinkedList(-4)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n2

print(listcycle(n1))




