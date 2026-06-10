#Given an array prices where prices[i] is the price of a stock
#on day i, return the maximum profit you can achieve.
#If no profit is possible, return 0.

prices = [7,1,5,3,6,4]
#Output: 5
#
#Input:  prices = [7,6,4,3,1]
#Output: 0

def stock_price(prices):
    min_price = prices[0]
    max_price = 0

    for i in range(len(prices)):
        if prices[i] < min_price:
         min_price =  prices[i]
        profit = prices[i] - min_price
        max_price = max(max_price, profit)
    return max_price
print(stock_price(prices))