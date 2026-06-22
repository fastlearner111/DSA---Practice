#Given an integer array nums and an integer k,
#return the k most frequent elements.
#Do NOT use sorting. Use bucket sort instead.
#
nums = [1,1,1,2,2,3]
k = 2
#Output: [1,2]
#
#Input:  nums = [1], k = 1
#Output: [1]

#Constraint: Must be O(n) time. No sorted() allowed.

def top_frequent(nums,k):
    count = {}

    for number in nums:
        if number in count:
            count[number] += 1
        else:
            count[number] = 1

    freq = [[] for i in range(len(nums) + 1)]

    for number, cnt in count.items():
        freq[cnt]. append(number)
        result = []
    for i in range(len(freq) - 1, 0, -1):
        for number in freq[i]:
            result.append(number)
            if len(result) == k:
                return result
print(top_frequent(nums,k))