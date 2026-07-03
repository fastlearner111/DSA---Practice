#Given an integer array nums, return True if any value appears 
#at least twice. Return False if every element is distinct.
#
nums = [1,2,3,1]
#Output: True
#
#Input:  nums = [1,2,3,4]
#Output: False
#
#Input:  nums = [1,1,1,3,3,4,3,2,4,2]
#Output: True

# Pattern - Hash
# data Structure needed - Set
# Approach = we need to see if the number is in set or not
# if no then return True then add, else return false

def contains_duplicate(nums):
    seen = set()

    for number in nums:
        
        if number in seen:
            return True
        seen.add(number)
    return False
print(contains_duplicate(nums))