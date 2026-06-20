class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev = None      # nothing behind first node
    curr = head      # start at the beginning

    while curr:
        next = curr.next    # save next before we break the link
        curr.next = prev    # reverse the pointer
        prev = curr         # move prev forward
        curr = next         # move curr forward

    return prev             # prev is now the new head

# Build list: 1 -> 2 -> 3 -> 4 -> 5
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

head = reverseList(n1)

# Print reversed list
current = head
while current:
    print(current.val, end=" -> ")
    current = current.next