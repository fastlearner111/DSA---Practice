#Given an integer array nums sorted in non-decreasing order, 
#remove duplicates in-place. Return the count of unique elements.

nums = [0,0,1,1,1,2,2,3,3,4]
#Output: 5

# the array is sorted, 
# we are counting
# we need to count from both side
# pattern -  two pointer, counting
# variable = k

def remove_duplicate(nums):
    k = 1

    for i in range(1,len(nums)):
        if nums[i] != nums[k-1]:
            nums[k] = nums[i]
            k += 1
    return k
print(remove_duplicate(nums))

