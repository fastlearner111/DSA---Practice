#Given an array nums of n+1 integers where each integer is in range [1,n],
#there is exactly one repeated number. Find and return it.
#Must use O(1) extra space. Cannot modify the array.
#
nums = [1,3,4,2,2]
#Output: 2
#
#Input:  nums = [3,1,3,4,2]
#Output: 3

def findDuplicate(nums):
    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow
print(findDuplicate(nums))