#Given an integer array nums, find a subarray that has the largest product, and return the product.
#The test cases are generated so that the answer will fit in a 32-bit integer.
#Note that the product of an array with a single element is the value of that element.
#
#Example 1:
nums = [2,3,-2,4]
#Output: 6
#Explanation: [2,3] has the largest product 6.

#Example 2:
#Input: nums = [-2,0,-1]
#Output: 0
#Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

def max_subarray(nums):
    max_sum = nums[0]
    current = nums[0]

    for i in range(1, len(nums)):
        current = max(nums[i], current + nums[i])
        max_sum = max(max_sum, current)

    return max_sum
print(max_subarray(nums)) 