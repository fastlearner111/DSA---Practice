#Given an array nums of size n, return the majority element.
#The majority element is the element that appears more 
#than n/2 times. You may assume the majority element 
#always exists in the array.

nums = [3, 2, 3]
#Output: 3

#Input:  nums = [2, 2, 1, 1, 2, 2, 1, 2]
#Output: 2

# first cretae a empty dict called count
# then create a loop
#if number in seen then count + 1
# if not then stays at 1 
# after the loop we use if and compare if count > n/2 if yes then return count

def majority_element(nums):
    count = {}

    for number in nums:
        if number in count:
            count[number] += 1
        else:
            count[number] = 1

    for number,freq in count.items():
        if freq > len(nums) / 2:
         return number        
    return number
print(majority_element(nums))
    
        