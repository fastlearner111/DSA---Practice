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

# 
def rotated_sorted(nums):
    left = 0
    right = len(nums) - 1
    

    while left < right:
        mid = (left + right) // 2
        # variable = ...
        # may be we need a result variable
        # i do know that if the num is < then we move pointer to left
        # else vice versa
        # Not sure what syntax to use to check
        # may be mid > right then left = mid + 1
        # then update the variable to mid
        if nums[left] == nums[right]:
            return nums[left]
        elif nums[mid] > nums[right]:
            left = mid + 1
       # result = min(result,nums[mid])
        elif nums[mid] < nums[right]:
            right = mid 
    return nums[left]
print(rotated_sorted(nums))