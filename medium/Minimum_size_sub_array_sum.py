#Given an array of positive integers nums and a positive integer target,
#return the minimal length of a subarray whose sum is >= target.
#If no such subarray, return 0.
#
#target = 7
#nums = [2,3,1,2,4,3]
#Output: 2  (subarray [4,3])
#
target = 4
nums = [1,4,4]
#Output: 1
#
#target = 11
#nums = [1,1,1,1,1,1,1,1]
#Output: 0

def isMinimum(nums, target):
    left = 0
    result = float('inf')
    total = 0

    for right in range(len(nums)):
        total += nums[right]
        while total >= target:
            result = min(result, right - left + 1)
            total -= nums[left]
            left += 1
    return result if result != float('inf') else 0
print(isMinimum(nums,target))