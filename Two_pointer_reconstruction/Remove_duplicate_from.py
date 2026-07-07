#Given sorted integer array nums, remove duplicates in-place.
#Return the number of unique elements k.
#
nums = [1,1,2]
#Output: 2, nums = [1,2,_]
#
#Input:  nums = [0,0,1,1,1,2,2,3,3,4]
#Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

#Pattern - Two Pointer
# Data Struct -
# Approach - 
# Big O -On, On

def return_unique(nums):
    k = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[k - 1]:
            nums[k] = nums[i]
            k += 1
    return k
print(return_unique(nums))