#Koko has piles of bananas and h hours to eat them all.
#Each hour she eats at most k bananas from one pile.
#Find the minimum k so she can finish in h hours.
#
piles = [3,6,7,11]
h = 8
#Output: 4
#
#Input:  piles = [30,11,23,4,20], h = 5
#Output: 30

# we need to find the minimum hours 
#  h = hours to eat
# piles 
# pattern is binary search
# we need two pointer left and right , left= 1, and right = max(piles)
# we need a total varibale to track the hour

def time_taken(piles,h):
    left = 1
    right = max(piles)
    result = float('inf')

    while left <= right:
        mid = (left + right) //  2
        hour = sum((pile + mid - 1) // mid for pile in piles)

        if hour <= h:
            result = mid
            right = mid - 1
        elif hour >= h:
            left = mid + 1
    return result
print(time_taken(piles,h))
        


                   