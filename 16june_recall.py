#You are given the heads of two sorted linked lists list1 and list2.
#Merge them into one sorted list and return the head.
#
list1 = [1,2,4]
list2 = [1,3,4]
#Output: [1,1,2,3,4,4]
#
#Input:  list1 = [], list2 = []
#Output: []


class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self. next = next

def mergelist(list1,list2):
        dummy = ListNode(0)
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1:
            current.next = list1
        else:
            current.next = list2

        return dummy.next

l1n1 = ListNode(1)
l1n2 = ListNode(2)
l1n3 = ListNode(3)
l1n1.next = l1n2
l1n2.next = l1n3

l2n1 = ListNode(1)
l2n2 = ListNode(3)
l2n3 = ListNode(4)
l2n1.next = l2n2
l2n2.next = l2n3

result = mergelist(l1n1,l2n1)

current = result
while current:
    print(current.val, end = ">")
    current = current.next

     
