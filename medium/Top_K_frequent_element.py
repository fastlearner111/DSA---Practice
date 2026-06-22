#Given an integer array nums and an integer k, 
#return the k most frequent elements in any order.

nums = [1,1,1,2,2,3]
k = 2
#Output: [1,2]
#
#Input:  nums = [1], k = 1
#Output: [1]

def top_frequent(nums,k):
    count = {}

    for number in nums:
        if number in count:
            count[number] += 1
        else:
            count[number] = 1

    return sorted(count, key = lambda x:count[x], reverse = True)[:k]

print(top_frequent(nums,k))