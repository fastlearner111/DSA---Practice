#Example 1:
nums = [9,1,4,2,3,3,7]
#Output: 4
#Explanation: The longest increasing subsequence is [1,2,3,7], which has a length of 4.

class Solution:
    def longest_increase(self, nums):
        if not nums:
            return 0

        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:

                  dp[i] = max(dp[i], dp[j] + 1 )
                  
        return max(dp)
