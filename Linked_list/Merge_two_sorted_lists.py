#You are given the heads of two sorted linked lists list1 and list2.
#Merge the two lists into one sorted list and return the head.
#
list1 = [1,2,4]
list2 = [1,3,4]
#Output: [1,1,2,3,4,4]
#
#Input:  list1 = [], list2 = []
#Output: []

class ListNode:
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = next

def mergeTwolists(list1, list2):
    dummy = ListNode()
    current = dummy

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        tail = 