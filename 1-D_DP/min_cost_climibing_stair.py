cost = [1,2,1,2,1,1,1]
#Output: 4

class Solution:
    def min_cost(self, cost):
        n = len(cost)

        prev2 = cost[0]
        prev1 = cost[1]

        for i in range(2, n):
            current = cost[i] + min(prev1, prev2)

            prev2 = prev1
            prev1 = current

        return min(prev1,prev2)