#Given an m x n matrix where each row is sorted and the first integer 
#of each row is greater than the last integer of the previous row.
#Return True if target exists in matrix, False otherwise.
#
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
#Output: True
#
#Input:  matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
#Output: False

def check_matrix(matrix, target):
    m = len(matrix)
    n = len(matrix[0])
    left = 0
    right = m * n - 1

    while left <= right:
        mid = (left + right) // 2
        row = mid // n
        column = mid % n
        value = matrix[row][column]

        if value == target:
            return True
        elif value > target:
            right = mid - 1
        elif value < target:
            left = mid + 1
    return False
print(check_matrix(matrix, target))