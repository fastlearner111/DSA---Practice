#Given an integer array nums and an integer val, remove 
#all occurrences of val in nums in-place. Return the 
#number of elements remaining that are not equal to val.


nums = [3, 2, 2, 3]
val = 3
#Output: 2, nums = [2, 2, _, _]

#Input:  nums = [0,1,2,2,3,0,4,2], val = 2
#Output: 5, nums = [0,1,4,0,3,_,_,_]


def remove_duplicate(nums, val):
    k = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k
print(remove_duplicate(nums, val))