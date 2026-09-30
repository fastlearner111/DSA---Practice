prices = [10,1,5,6,7,1]
#Output: 6

class Solution:
    def stock_price(self, prices):
        left = 0
        right = 1
        max_profit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                left = right

            right += 1
        return max_profit