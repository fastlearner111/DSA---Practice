points = [[0,2],[2,0],[2,2]]
k = 2

#Output: [[0,2],[2,0]]

import heapq

class Solution:
    def closet(self, points,k):
        heap = []

        for x,y in points:
            dist = -(x ** 2 + y ** 2)
            heapq.heappush(heap, (dist,x,y))

            if len(heap) > k:
                heapq.heappop(heap)
        return [[x,y] for dist, x, y in heap]
