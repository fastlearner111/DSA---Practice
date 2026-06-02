#Given an array of integers, return the majority element.
#The element appears more than n/2 times.

nums = [4, 4, 2, 4, 3, 4, 2]
#Output: 4

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