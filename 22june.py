#Given an unsorted array of integers, return the length of the 
#longest consecutive sequence.
#Must be O(n) time.
#
nums = [100,4,200,1,3,2]
##Output: 4  (sequence: 1,2,3,4)
#
#Input:  nums = [0,3,7,2,5,8,4,6,0,1]
#Output: 9  (sequence: 0,1,2,3,4,5,6,7,8)
#
#Input:  nums = []
#Output: 0


def longest(nums):
    if not nums:
        return 0
    numSet = set(nums)
    result = 0

    for number in numSet:
        if number - 1 not in numSet:
            length = 1
            while (length + number) in numSet:
                length += 1
            result = max(result,length)
    return result
print(longest(nums))