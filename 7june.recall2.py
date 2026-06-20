#Given an integer array nums, return true if any value appears
#at least twice in the array, and return false if every element
#is distinct.
#
nums = [1,2,3,1]
#Output: True

#Input:  nums = [1,2,3,4]
#Output: False

def check_duplicate(nums):
    seen = set()

    for number in nums:
        if number in seen:
            return True
        seen.add(number)
    return False
print(check_duplicate(nums))