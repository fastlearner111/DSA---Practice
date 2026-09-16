import heapq
class Solution:
    def meeting(self, intervals):

        intervals.sort(key=lambda i: i[0])

        heap = []

        for start, end in intervals:
            if heap and start >= heap[0]:
                heapq.heappop(heap)

            heapq.heappush(heap, end)

        return len(heap) 