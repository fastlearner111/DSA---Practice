nums = [2,4,-3,5]
#Output: 8

class Solution:
    def maximum_product(self, nums):

        res = max(nums)
        curr_max = 1
        curr_min = 1

        for n in nums:
            temp = curr_max * n

            curr_max = max(n, temp, curr_min *n)
            curr_min = max(n, temp, curr_min *n)

            res = max(res, curr_max)

        return res