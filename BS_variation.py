#Given a sorted array of integers nums and a target, return the
#index where target should be inserted in order to keep the array
#sorted. If target already exists, return its index.

nums = [1,3,5,6]
target = 5
#Output: 2

def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    return left
print(binary_search(nums,target))