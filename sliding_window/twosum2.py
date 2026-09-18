numbers = [1,2,3,4]
target = 3

#Output: [1,2]

def two_sum(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left + 1, right - 1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return current_sum