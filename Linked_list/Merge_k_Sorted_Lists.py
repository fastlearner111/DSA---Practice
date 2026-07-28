#Merge k Sorted Lists

#You are given an array of k linked-lists lists, each 
# linked-list is sorted in ascending order.
#
#Merge all the linked-lists into one sorted linked-list 
# and return it.

#Example 1:
#Input: lists = [[1,4,5],[1,3,4],[2,6]]
#Output: [1,1,2,3,4,4,5,6]
#Explanation: The linked-lists are:
#[
#  1->4->5,
#  1->3->4,
#  2->6
#]
#merging them into one sorted linked list:
#1->1->2->3->4->4->5->6

#Example 2:
#Input: lists = []
#Output: []

#Example 3:
#Input: lists = [[]]
#Output: []

#Constraints:
#k == lists.length
#0 <= k <= 104
#0 <= lists[i].length <= 500
#-104 <= lists[i][j] <= 104
#lists[i] is sorted in ascending order.
#The sum of lists[i].length will not exceed 104.

#Step 1: Push the first node of each list into a min‑heap
#Step 2: Pop the smallest node from the heap and attach it to the result list
#Step 3: Push the next node from the same list into the heap

import heapq

class ListNode:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    heap = []
    for node in lists:
        if node:
            heapq.heappush(heap, (node.val, node))

    dummy = ListNode(0)
    tail = dummy


    while heap:
        val, node = heapq.heappop(heap)
        tail.next = node
        tail = tail.next

        if node.next:
            heapq.heappush(heap, (node.next.val, node.next))

    return dummy.next


# Helpers
def build_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head

def print_list(head):
    curr = head
    while curr:
        print(curr.val, end="->")
        curr = curr.next
    print()

# Test
l1 = build_list([1,4,5])
l2 = build_list([1,3,4])
l3 = build_list([2,6])

merged = mergeKLists([l1, l2, l3])
print_list(merged)