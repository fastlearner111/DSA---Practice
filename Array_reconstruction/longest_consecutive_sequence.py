#Given unsorted array of integers, return length of longest 
#consecutive sequence. Must be O(n) time.
#
nums = [100,4,200,1,3,2]
#Output: 4  (sequence: 1,2,3,4)
#
#Input:  nums = [0,3,7,2,5,8,4,6,0,1]
#Output: 9

#Pattern - Hash and Hash Table
# Data Structure - Set
# Approach - 
# big O - On, On

def longest(nums):
    if not nums:
        return 0
    
    numSet = set(nums)
    result = 0

    for number in numSet:
        if number - 1 not in numSet:
            length = 1
            while (number + length) in numSet:
                length += 1
            result = max(result, length)
    return result
print(longest(nums))