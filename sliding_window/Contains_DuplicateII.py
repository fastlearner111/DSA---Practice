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

def containsDuplicate(nums,k):
    window = set()
    l = 0

    for r in range(len(nums)):
        # if the winodw size exceeds from the left shrink from the left

        if r - l > k:
            window.remove(nums[l])
            l += 1

        # if current number already in window --- duplicate within k
        if nums[r] in window:
            return True
        
        # Add current number to window
        window.add(nums[r])
    return False
print(containsDuplicate(nums,k))