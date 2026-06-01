#Given an integer array nums and an integer val, remove 
##all occurrences of val in-place. Return the count of 
#remaining elements.

nums = [1, 2, 6, 3, 6, 6]
val = 6
#Output: 3

def remove_occurence(nums,val):
    
    k = 0

    for i in range(len(nums)):
        
     if nums[i] != val:
      nums[k] = nums[i]
      k += 1
    return k
print(remove_occurence(nums,val))
