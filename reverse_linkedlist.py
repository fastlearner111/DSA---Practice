#Given the head of a singly linked list, reverse the list
#and return the reversed list.

head = [1,2,3,4,5]
#Output: [5,4,3,2,1]

#Input:  head = [1,2]
#Output: [2,1]

class ListNode:

     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3

current = node1
while current:
    print(current.val(-1))
    current = current.next        