#Given a sorted array nums, remove duplicates in-place
#and return the count of unique elements.

nums = [1,1,2,3,3]
#Output: 3

def remove_duplicate(nums):
    k = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[k-1]:
            nums[k] = nums[i]
            k += 1
    return k
print(remove_duplicate(nums))