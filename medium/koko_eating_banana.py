#Koko has piles of bananas. She has h hours to eat all bananas.
#Each hour she eats at most k bananas from one pile.
#Find the minimum k so she can finish in h hours.
#
piles = [3,6,7,11]
h = 8
#Output: 4
#
#Input:  piles = [30,11,23,4,20], h = 5
#Output: 30
#
#Input:  piles = [30,11,23,4,20], h = 6
#Output: 23

def findBanana(piles,h):
    left = 1
    right = max(piles)

    while left <= right:
        mid = (left + right) // 2
        hours = sum((pile + mid - 1) // mid for pile in piles)

        if hours <= h:
            result = mid
            right = mid - 1
        elif hours > h:
            left = mid + 1
    return result
print(findBanana(piles,h))