#Given an array of integers, return true if any value 
#appears at least twice, false if all elements are distinct.

nums = [7, 3, 9, 3, 1]
#Output: True

def check_duplicate(nums):
    seen = set()
    
    for number in nums:
        if number in seen:
            return True
        seen.add(number)
        
    return False
print(check_duplicate(nums))

