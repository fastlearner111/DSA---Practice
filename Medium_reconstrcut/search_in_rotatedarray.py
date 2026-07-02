#Given a rotated sorted array and a target, return the index of target.
#Return -1 if not found.
#
nums = [4,5,6,7,0,1,2]
target = 0
#Output: 4
#
#Input:  nums = [4,5,6,7,0,1,2], target = 3
#Output: -1
#
#Input:  nums = [1], target = 0
#Output: -1

def sorted_array(nums,target):
    left = 0
    right = len(nums) - 1
    result = {}

    while left < right:
        mid = (left + right) // 2

        if nums[left] == nums[right]:
            return nums[left]
        elif nums[left] > target:
            right = mid - 1
        elif nums[right] > target:
            left = mid + 1
    return -1 
print(sorted_array(nums, target))