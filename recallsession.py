#Given an integer array nums and integer k, return true if
#any value appears at least twice within k indices of itself.

nums = [1,2,3,1]
k = 3
Output: True

#Input:  nums = [1,2,3,1,2,3], k = 2
#Output: False

def count_duplicate(nums, k):
    seen = {}

    for i, number in enumerate(nums):
        if number in seen:
            if abs(i - seen[number]) <= k:
                return True
        seen[number] = i
    return False
print(count_duplicate(nums,k))