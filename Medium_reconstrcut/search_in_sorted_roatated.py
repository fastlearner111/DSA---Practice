#Given a rotated sorted array and a target integer, return the index of target.
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

# so i need to find the index , not the number, 
# questions ones me to find the target indext
# so as always there is gonna be three conditions, 
# one == , return the index, and set result =mid
# second >, in this we move the pointer from right = mid + 1
# third <, in this we move the pointer from left  = mid - 1
# pattern is Binary Search
# 

def sorted_rotated(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] <= target < nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
print(sorted_rotated(nums, target)) 

                