nums = [2, 7, 11, 15]
target = 9

def two_sum(nums, target):
    seen = {}
    for index, number in enumerate(nums):
        complement = target - number
        if complement in seen:
            return [seen[complement], index]
        seen[number] = index
    return []

print(two_sum(nums, target))