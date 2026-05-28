#Given an array of integers, return true if any value 
#appears at least twice, false if all elements are distinct.

nums = [1, 2, 3, 1]
#Output: True

#Input:  nums = [1, 2, 3, 4]
#Output: False

#Constraints:
#- 1 <= nums.length <= 10^5
#- -10^9 <= nums[i] <= 10^9

# 

def check_duplicate(nums):

    seen = set()

    for number in nums:
        if number in seen:
            return True
        seen.add(number)
        
    return False
print(check_duplicate(nums))