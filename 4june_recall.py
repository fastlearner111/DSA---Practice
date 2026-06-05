#Given an integer array nums and an integer k, return true 
#if there are two distinct indices i and j such that 
#nums[i] == nums[j] and abs(i - j) <= k.

nums = [1,2,3,1,2,3]
k = 2
#Output: False

#Input:  nums = [1,0,1,1], k = 1
#Output: True

def contains_duplicate(nums, k):
    seen = {}

    for i, number in enumerate(nums):
        if number in seen:
           if  abs(i - seen[number]) <= k:
            return True
        seen[number] = i
    return False
print(contains_duplicate(nums,k))