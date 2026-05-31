#Given an integer array nums and an integer val, remove 
#all occurrences of val in-place. Return the count of 
#remaining elements.

nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
#Output: 5

# first we need a variable k
# then we need a loop range
# then we see if current nums is equal to val or not
# if not then we update the value of k with current value of i, 
# then k+= 1

def remove_duplicate(nums,val):

    k = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k
print(remove_duplicate(nums,val))
