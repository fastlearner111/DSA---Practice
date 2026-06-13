#Given a non-negative integer x, return the square root of x
#rounded down to the nearest integer.

x = 8
#Output: 2
#
#Input:  x = 4
#Output: 2

def square_root(x):
    left = 1
    right = x
    result = 0

    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            result = mid
            return mid
        elif mid * mid < x:
            result = mid
            left = mid + 1
        elif mid * mid > x:
            right = mid - 1
    return result
print(square_root(x))