
#You are given an array prices where prices[i] is the price 
#of a given stock on the i-th day.

#You want to maximize your profit by choosing a single day 
#to buy and one different day in the future to sell.

#eturn the maximum profit. If no profit is possible, return 0.

prices = [7,1,5,3,6,4]
#Output: 5  (buy at 1, sell at 6)
#
#Input:  prices = [7,6,4,3,1]
#Output: 0  (prices only decrease)

#we update min price, then we calculate profuit then max profut

def best_time(prices):

    min_value = prices[0]
    max_profit = 0 

    for i in range(len(prices)):
        if  prices[i]< min_value:
            min_value = prices[i]
        profit = prices[i] - min_value
        max_profit = max(max_profit, profit)
    return max_profit
print(best_time(prices)) 

   

