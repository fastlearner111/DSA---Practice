head = [1,2,3,4]
index = 1

#Output: true

class ListNode:
    def __init__(self, val = 0, left = None):
        self.val = val
        self.left = val

def hasCycle(head):
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    return False
