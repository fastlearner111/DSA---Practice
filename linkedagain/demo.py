class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def reorder(head):
    if not head:
        return 

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next

    prev = None
    curr = slow.next
    slow.next = None

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    first = head
    second = prev

    while second:
        tmp1 = first.next
        tmp2 = second.next

        first.next = second
        second.next = tmp1

        first = tmp1
        second = tmp2
        
    return head