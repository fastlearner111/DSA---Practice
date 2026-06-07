#Given an array of integers nums which is sorted in ascending order,
#and an integer target, return the index of target if it exists,
#otherwise return -1.
#You must write an algorithm with O(log n) runtime complexity.

nums = [-1,0,3,5,9,12]
target = 9
#Output: 4

#Input:  nums = [-1,0,3,5,9,12], target = 2
#Output: -1

#pattern : binary search, variable : left, right, mid, steps,:
#  first we use while loop, then we use 3 if first for nums[mid] == target found,
#  second for less than target in this we move left +1,
#  and the last gretaer than we move right -=1 , then  return nums

def binary_search(nums, target):
    left = 0 
    right = len(nums) - 1
    #mid  = (left + right) // 2

    while left <= right:
        mid  = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    return -1
print(binary_search(nums,target))