def search(matrix, target):
    if not matrix or not matrix[0]:
        return False

    rows = len(matrix)
    cols = len(matrix[0])

    left = 0
    right = (rows - cols) - 1

    while left <= right:
        mid = (left + right) // 2

        row = mid // cols
        cols = mid % cols

        if mid == target:
            return True
        elif mid > target:
            left = mid + 1
        else:
            right = mid - 1
    return False

