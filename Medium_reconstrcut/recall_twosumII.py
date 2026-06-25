#Given a 1-indexed sorted array, find two numbers that add up to target.
#Return their 1-indexed positions. Must use O(1) space.
#
numbers = [2,7,11,15]
target = 9
#Output: [1,2]
#
#Input:  numbers = [2,3,4], target = 6
#Output: [1,3]
#
#Input:  numbers = [-1,0], target = -1
#Output: [1,2]

def two_sum(numbers,target):
    left = 0
    right = len(numbers) - 1
    
    while left < right:
        sum = numbers[left] + numbers[right]
        if sum == target:
            return ([left + 1, right + 1])
        elif sum > target:
            right -= 1
        elif sum < target:
            left += 1
print(two_sum(numbers,target))