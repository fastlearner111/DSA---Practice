stones = [2,3,6,2,4]
#Output: 1

import heapq

class Solution:
    def stone_weight(self,stone):
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            first = -heapq.heappop(max_heap)
            second = -heapq.heappop(max_heap)

            if first > second:
                leftover = first - second
                heapq.heappush(max_heap, -leftover)

        return -max_heap[0] if max_heap else 0