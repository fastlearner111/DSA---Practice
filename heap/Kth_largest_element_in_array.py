#Given an unsorted array of integers nums and an integer k, 
#return the kth largest element in the array.
#By kth largest element, we mean the kth largest element
#in the sorted order, not the kth distinct element.

#Example 1:
nums = [2,3,1,5,4]
k = 2

import heapq
class Solution:
    def largest_element(self, nums, k):
        heap = []

        for num in nums:
            heapq.heappush(heap,num)
            if len(num) > k:
                heapq.heappop(num)
        return heap[0]