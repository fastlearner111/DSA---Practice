#Given an integer array nums, remove all duplicate 
#values and return the count of unique elements.
#The relative order must be maintained.

nums = [1, 1, 2, 3, 3, 4]
#Output: 4, nums = [1, 2, 3, 4, _, _]

def remove_element(nums):

    k = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[k-1]:
            nums[k] = nums[i]
            k += 1
    return k
print(remove_element(nums))