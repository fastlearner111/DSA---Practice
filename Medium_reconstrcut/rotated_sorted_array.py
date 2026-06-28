#Given a rotated sorted array of unique integers, find the minimum element.
#
nums = [3,4,5,1,2]
#Output: 1
#
#Input:  nums = [4,5,6,7,0,1,2]
#Output: 0
#
#Input:  nums = [11,13,15,17]
#Output: 11

# so for this we need to find the lowest number from the array
# so that means we first divide it and then compare with mid if high then move right pointer 
# if not the move the left pointer
# then we 

def rotated_array(nums):
    left = 0
    right = len(nums) - 1
    

    while left < right:
        mid = (left + right) // 2
        if nums[left] == nums[right]:
            return nums[left]
        elif nums[mid] > nums[right]:
            left = mid + 1
        elif nums[mid] < nums[left]:
            right = mid
    return nums[left]
print(rotated_array(nums))
