#Given an array of integers, return the majority element.
#The element appears more than n/2 times.

nums = [3, 3, 4, 3, 2, 3, 1]
#Output: 3

def check_majority(nums):

    count = {}

    for number in nums:
        if number in count:
            count[number] += 1
        else:
            count[number] = 1

    for number, freq in count.items():
        if freq > len(nums) / 2:
            return number 
    return -1
print(check_majority(nums))
