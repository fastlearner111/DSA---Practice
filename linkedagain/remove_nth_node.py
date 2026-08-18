head = [1,2,3,4]
n = 2

#Output: [1,2,4]

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def removeNthfromEnd(head):
    dummy = ListNode(0, head)
    left = dummy
    right = head

    for _ in range(n):
        right = right.next

    while right:
        left = left.next
        right = right.next

    left.next = left.next.next

    return dummy.next