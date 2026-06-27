#Given an m x n matrix where each row is sorted and the first integer 
#of each row is greater than the last integer of the previous row.
#Return True if target exists, False otherwise.
#
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
#Output: True
#
#Input:  matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
#Output: False

# m = row, n = column, 
# this is binary search
# the aproach to this problem is 
# first we need to two poniters left and right and then 
# then we need m and n, which is the length of matrix, one for row and other for column
# the we use while loop
# first we find mid , sum variabel where we make this eaaier to solve ,
# then == then result = mid, return True, else > then right = mid - 1
# else < left = mid - 1, then return False outside this then print

def two_d(matrix,target):
    m = len(matrix)
    n = len(matrix[0])
    left = 0
    right = m * n - 1
    result = 0

    while left <= right:
        mid = (left + right) // 2
        row = mid // n
        column = mid % n
        total = matrix[row][column]
        if total == target:
            result = mid
            return True
            
        elif total > target:
            right = mid - 1
        elif total < target:
            left = mid + 1
    return False
print(two_d(matrix,target))