stones = [2,3,6,2,4]

#Output: 1

import heapq

def laststone(self,stones):
    stones = [-s for s in stones]
    heapq.heapify(stones)

    while len(stones) > 1:
        stone1 = -heapq.heappop(stones)
        stone2 = -heapq.heapop(stones)

        if stone1 != stone2:
            heapq.heappush(stones, -(stone1 - stone2))

    return -stones[0] if stones else 0 