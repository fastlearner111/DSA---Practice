#Given an integer array nums, return an array output where 
#output[i] is the product of all elements except nums[i].
#You must solve it without using division and in O(n) time.
#
nums = [1,2,3,4]
#Output: [24,12,8,6]
#
#Input:  nums = [2,3]
#Output: [3,2]

def productArray(nums):
    n = len(nums)
    output = [1] * n

    for i in range(1, n):
        output[i] = output[i-1] * nums[i-1]

    suffix = 1
    for i in range(n-1, -1 , -1 ):
        output[i] *= suffix
        suffix = suffix * nums[i]
    return output
print(productArray(nums))
