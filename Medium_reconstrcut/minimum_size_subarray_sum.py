#Given array of positive integers nums and integer target,
#return minimal length of subarray whose sum >= target.
#Return 0 if no such subarray exists.
#
target = 7
nums = [2,3,1,2,4,3]
#Output: 2
#
#Input:  target = 4, nums = [1,4,4]
#Output: 1
#
#Input:  target = 11, nums = [1,1,1,1,1,1,1,1]
#Output: 0

# positive int nums, int target, return minimal length, sum should be gretaer than or equal to target
# retunr 0 if no arr exist, 

def minimum_size(nums,target):
    left = 0
    total = 0
    result = float('inf')
    
    for right in range(len(nums)):
        total += nums[right]
        while total >= target:
            result = min(result, right - left + 1)
            total -= nums[left]
            left += 1
    return result if result != float('inf') else 0
print(minimum_size(nums, target))