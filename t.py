def remove_duplicates(nums):
    left = 0
    
    for right in range(len(nums)):
        if nums[right] != nums[left]:
            nums[left] = nums[right]
            left += 1
    
    return left

print(remove_duplicates([1,1,2,3,3]))