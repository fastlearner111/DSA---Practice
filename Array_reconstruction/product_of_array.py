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
def product_array(nums):
    n = len(nums)
    output = [1] * n

    for i in range(1,n):
        output[i] = output[i - 1] * nums[i - 1]

    suffix = 1
    for i in range(n - 1, -1, -1):
        output[i] *= suffix
        suffix = suffix * nums[i]
    return output
print(product_array(nums))
