#We are playing a guessing game. I pick a number from 1 to n.
#You call a guess(num) API which returns:
##-1 if num is higher than the picked number
## 1 if num is lower than the picked number
## 0 if num is correct
##
#Return the number I picked.
#
n = 10
pick = 6
#Output: 6



def guess(num):
    if num > pick:
        return -1
    elif num < pick:
        return 1
    elif num == pick:
        return 0 

def guess_number(n,pick):
    left = 1
    right = n

    while left <= right:
        mid = (left + right) // 2
        result = guess(mid)
        if result == 0:
            return mid
        elif result == 1:
            left = mid + 1
        elif result == -1:
            right = mid - 1
    return result 
print(guess_number(n,pick))
