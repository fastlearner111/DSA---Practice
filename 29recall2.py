#Given an array of integers and a target, return the 
#indices of the two numbers that add up to the target.

nums = [5, 3, 7, 2]
target = 9
#Output: [2, 3]

def check_index(nums,target):
    seen = {}

    for index, number in enumerate(nums):
        complement = target - number
        if complement in seen:
            return [seen[complement], index]
        else:
            seen[number] = index
    return []
print(check_index(nums,target))