#Given an array of integers nums which is sorted in ascending order,
#and an integer target, return the index of target if it exists,
#otherwise return -1.
#You must write an algorithm with O(log n) runtime complexity.

nums = [-1,0,3,5,9,12]
target = 9
#Output: 4
#
#Input:  nums = [-1,0,3,5,9,12], target = 2
#Output: -1

def b_s(nums,target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right ) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
    return -1
print(b_s(nums,target))