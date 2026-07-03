#Given an integer array nums and integer k, return the k most frequent elements.
#
nums = [1,1,1,2,2,3]
k = 2
#Output: [1,2]
#
#Input:  nums = [1], k = 1
#Output: [1]

# Pattern - Hash and Hash Table
# data Structure - dict maybe
# Approach - so we need to check which number is repeated how many times
# we do this by frequensy check then we set a condition to check the top 2 number and then rturn them 
# Big O -  On , On

def frequency_check(nums, k):
    count = {}

    for number in nums:
        if number in count:
            count[number] += 1
        else:
            count[number] = 1
    return sorted(count, key = lambda x: count[x], reverse = True)[:k]
print(frequency_check(nums,k))