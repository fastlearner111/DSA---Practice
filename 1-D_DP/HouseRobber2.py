nums = [2,9,8,3,6]

class Solution:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]

        def rob_linear(houses):
            prev2 = 0
            prev1 = 0

            for num in houses:
                current = max(prev1, num + prev2)

                prev2 = prev1
                prev1 = current
            
            return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))