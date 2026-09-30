intervals = [(0,40),(5,10),(15,20)]
#Output: 2

import heapq
class Solution:
    def meeting2(self, intervals):
        intervals.sort(key = lambda x: x[0])
        minHeap = []

        for start, end in intervals:
            if minHeap and minHeap[0] <= start:
                heapq.heappop(minHeap)

            heapq.heappush(minHeap,end)

        return len(minHeap)
    
sol = Solution()
print(sol.meeting2(intervals))