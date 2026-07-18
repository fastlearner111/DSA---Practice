#Given an integer array nums and an integer k, 
#return the k most frequent elements in any order.

nums = [1,1,1,2,2,3]
k = 2
#Output: [1,2]
#
#Input:  nums = [1], k = 1
#Output: [1]

from collections import Counter

def topk(nums, k):

    freq = Counter(nums)

    buckets = [[] for _ in range(len(nums) + 1)]

    for num, count in freq.items():
        buckets[count].append(num)

    
    result = []

    for i in range(len(buckets) - 1, -1, -1):
        for number in buckets[i]:
            result.append(number)
            if len(result) == k:
                return result
            
print(topk(nums, k))