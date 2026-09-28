nums = [2,3,1,5,4]
k = 2

#Output: 4

import heapq
class Solution:
    def largest_num(self, nums, k):
        heap = []

        for num in nums:
            heapq.heappush(heap,num)

            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]