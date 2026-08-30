stones = [2,3,6,2,4]

#Output: 1

import heapq

class Solution:
    def lastStoneWeight(self, stones):

        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)

            if first != second:
                diff = first - second
                heapq.heappush(stones, -diff)

        return -stones[0] if stones else 0
