#Given an integer array nums and an integer k, return true 
#if there are two distinct indices i and j in the array such 
#that nums[i] == nums[j] and abs(i - j) <= k.

nums = [1,2,3,1] 
k = 3
#Output: True

#Input:  nums = [1,0,1,1], k = 1
#Output: True

#Input:  nums = [1,2,3,1,2,3], k = 2
#Output: False

##Loop through every element with its index
#If the element is already in the dictionary — 
# check if the distance between current index and stored index is <= k
#If yes — return True
#If no — update the dictionary with the new index
#If element not in dictionary — add it

def contians_duplicate(nums, k):
    seen = {}

    for i, number in enumerate(nums):
        if number in seen:
            if abs(i - seen[number]) <= k:
              return True
            seen[number] = i  
        else:
          seen[number] = i
    return False
print(contians_duplicate(nums,k))




