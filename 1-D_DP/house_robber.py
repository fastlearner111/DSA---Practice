nums = [2,9,8,3,6]
#Output: 16

class Solution:
    def house_robber(self, nums):
        prev1 = 0
        prev2 = 0

        for num in nums:
            current = max(prev1, num + prev2)

            prev2 = prev1
            prev1 = current

        return prev1