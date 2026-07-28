#Given integer array nums, return array output where 
#output[i] is the product of all elements except nums[i].
#No division allowed. Must be O(n) time.
#
nums = [1,2,3,4]
#Output: [24,12,8,6]
#
#Input:  nums = [2,3]
#Output: [3,2]

# Pattern - Prefix / Suffix Product
# Data Structure - output array (no extra space)
# Approach - left pass stores prefix products, right pass multiplies suffix products
# Big O - O(n) time, O(1) space (output array doesn't count

#  
def product_except_self(nums):
    result = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        result[i] = prefix
        prefix += nums[i]

    suffix = 1
    for i in range(len(nums) -1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result
print(product_except_self(nums))