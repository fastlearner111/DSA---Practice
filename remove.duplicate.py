#Given an integer array nums sorted in non-decreasing order, 
#remove the duplicates in-place such that each unique element 
#appears only once. Return the number of unique elements.

nums = [1, 1, 2, 3, 3]
#Output: 2, nums = [1, 2, _]

#Input:  nums = [0,0,1,1,1,2,2,3,3,4]
#Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

def remove_duplicate(nums):
    k = 1
    

    for i in range(1, len(nums)):
        if nums[i] != nums[k-1]:
            nums[k] = nums[i]
            k += 1
    return nums[:k]
print(remove_duplicate(nums))

