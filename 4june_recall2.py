#Given an array prices, return the maximum profit 
#from buying and selling stock once.

prices = [1,4,2,7,3,9]
#Output: 8

def profit_calculate(prices):

    min_value = prices[0]
    max_profit = 0

    for i in range(len(prices)):
      if prices[i] < min_value:
        min_value = prices[i]
      profit = prices[i] - min_value
      max_profit = max(max_profit, profit)
    return max_profit
print(profit_calculate(prices))