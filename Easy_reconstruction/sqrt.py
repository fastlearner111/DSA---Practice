#Given a non-negative integer x, return the square root of x 
#rounded down to the nearest integer.
#Do not use any built-in exponent function or operator.
#
x = 4
#Output: 2
#
#Input:  x = 8
#Output: 2  (sqrt(8) = 2.82, rounded down = 2)
#
#Input:  x = 0
#Output: 0

def sqr(x):
    left = 0
    right = x
    result = 0

    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            result = mid
            return mid
        elif mid * mid < x:
            result = mid
            left = left + 1
        elif mid * mid > x:
            right = right - 1
    return result
print(sqr(x))