#Given integer array nums and integer k, return the k most frequent elements.
#
nums = [1,1,1,2,2,3]
k = 2
#Output: [1,2]
#
#Input:  nums = [1], k = 1
#Output: [1]

def top_k(nums,k):
    seen = {}

    for num in nums:
        if num in seen:
            seen[num] += 1
        else:
            seen[num] = 1
    return sorted(seen, key=lambda x:seen[x] ,reverse = True)[:k]
print(top_k(nums,k))