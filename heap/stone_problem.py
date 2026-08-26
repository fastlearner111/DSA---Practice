stones = [2,3,6,2,4]

#Output: 1

import heapq

class Solution:
    def lastStoneWeight(self, stones):

        # Python only has min-heap, so we invert values to simulate max-heap
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            first = -heapq.heappop(max_heap)  # heaviest
            second = -heapq.heappop(max_heap) # second heaviest

            if first != second:
                heapq.heappush(max_heap, -(first - second))

        return -max_heap[0] if max_heap else 0
