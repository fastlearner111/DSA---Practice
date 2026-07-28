#Reorder List
#
#You are given the head of a singly linked-list. 
#The list can be represented as:
#
#L0 → L1 → … → Ln - 1 → Ln
#Reorder the list to be on the following form:
#
#L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
#You may not modify the values in the list's nodes. 
#Only nodes themselves may be changed.

#Example 1:
#Input: head = [1,2,3,4]
#Output: [1,4,2,3]
#
#Example 2:
#Input: head = [1,2,3,4,5]
#Output: [1,5,2,4,3]
# 

#Constraints:
#The number of nodes in the list is in the range [1, 5 * 104].
#1 <= Node.val <= 1000



class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def reorder_list(head):
    slow = head
    fast = head

    # Step 1: find middle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: reverse second half
    second = slow.next
    slow.next = None

    prev = None
    while second:
        temp = second.next
        second.next = prev
        prev = second
        second = temp

    # Step 3: merge two halves
    first = head
    second = prev

    while second:
        tmp1 = first.next
        tmp2 = second.next

        first.next = second
        second.next = tmp1

        first = tmp1
        second = tmp2

# Build test list
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n1.next = n2
n2.next = n3
n3.next = n4

# Run reorder
reorder_list(n1)

# Print result
current = n1
while current:
    print(current.val, end=">")
    current = current.next
