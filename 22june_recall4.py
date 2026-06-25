#Given an unsorted array of integers, return the length of the 
#longest consecutive sequence. Must be O(n) time.
#
nums = [100,4,200,1,3,2]
#Output: 4
#
#Input:  nums = []
#Output: 0

def longestseq(nums):
    if not nums:
        return 0
    numSet = set(nums)
    result =  0 

    for number in numSet:
        if number - 1 not in numSet:
            length = 1
            while(length + number) in numSet:
                length += 1
            result =   max(result,length)
    return result
print(longestseq(nums))