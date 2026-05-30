##Given an integer array nums and an integer val, remove 
#all occurrences of val and return the modified array 
#itself, not just the count.

nums = [3, 2, 2, 3]
val = 3
#Output: [2, 2]

def remove_duplicate(nums,val):
    k = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return nums[0:k]
print(remove_duplicate(nums,val)) 