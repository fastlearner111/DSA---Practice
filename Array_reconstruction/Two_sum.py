#Given an array of integers nums and an integer target, return 
#indices of the two numbers that add up to target.
#
nums = [2,7,11,15]
target = 9
#Output: [0,1]
#
#Input:  nums = [3,2,4], target = 6
#Output: [1,2]
#
#Input:  nums = [3,3], target = 6
#Output: [0,1]

# Pattern - Hash & Hash Table
# Data Structure - dict
# Approach -  so to find the target, we need to first find the complement
# complement stores the difference of target - number
# then we need to check if the complement is in the dict or not
# if yes then return the index
# else we need to move to next index
# then outside the loop and we return []
#Big O -  On, On

def two_sum(nums, target):
    seen = {}

    for index, number in enumerate(nums):
        complement  = target - number
        if complement in seen:
            return ([seen[complement], index])
        else:
            seen[number] = index
    return []
print(two_sum(nums, target))