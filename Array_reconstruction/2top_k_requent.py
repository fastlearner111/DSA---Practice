#Given an integer array nums and integer k, return the k most frequent elements.
#
nums = [1,1,1,2,2,3]
k = 2
#Output: [1,2]
#
#Input:  nums = [1], k = 1
#Output: [1]

#Step 1: build frequency map → O(n)
#Step 2: build and fill buckets → O(n)
#Step 3: scan buckets → O(n)

#time and space both On

def top_k_frequent(nums,k):
    freq = {}

    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1


        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in freq.items():
            buckets[count].append(num)

        result = []
        for i in range(len(buckets) -1, -1, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
                