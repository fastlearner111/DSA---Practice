import heapq

class Solution:
    def __init__(self):
        self.small = []
        self.large = []

        def addnum(self,num):
            heapq.heappush(self.num, -num)

            if self.small and self.large and (-self.small[0] > self.large[0]):
                val = -heapq.heappop(self.small)
                heapq.heappush(self.large, val)

            if len(self.small) > len(self.right) + 1:
                val = -heapq.heappop(self.small)
                heapq.heappush(self.large, val)
            elif len(self.large) > len(self.small):
                val = heapq.heappop(self.large)
                heapq.heappop(self.small, val)

        def findMedian(self):
            if len(self.small) > len(self.right):
                