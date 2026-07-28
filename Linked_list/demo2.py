class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")


def mergeKLists(lists):
    import heapq

    heap = []
    counter = 0

    for node in lists:
        if node:
            heapq.heappush(heap, (node.val, counter, node))
            counter += 1

    dummy = ListNode()
    curr = dummy

    while heap:
        val, _, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next

        if node.next:
            heapq.heappush(heap, (node.next.val, counter, node.next))
            counter += 1

    return dummy.next


# Test
l1 = build_list([1, 4, 5])
l2 = build_list([1, 3, 4])
l3 = build_list([2, 6])

merged = mergeKLists([l1, l2, l3])
print_list(merged)
