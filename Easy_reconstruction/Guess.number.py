#I pick a number from 1 to n. You call guess(num) API which returns:
#-1 if your guess is too high
# 1 if your guess is too low
# 0 if correct
#
#Return the number I picked.
#
n = 10
pick = 6
#Output: 6
#
#Input:  n = 1, pick = 1
#Output: 1

def guess(num):
    if num > pick:
        return - 1
    elif num < pick:
        return 1
    elif num == pick:
        return 0
    
def guessNumber(n):
    left = 1
    right = n

    while left <= right:
        mid = (left + right) // 2
        result = guess(mid)
        if result == 0:
            return mid
        elif result == -1:
            right = mid - 1
        elif result == 1:
            left = mid + 1
    return -1
print(guessNumber(n))