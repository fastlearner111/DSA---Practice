#Given an array of integers, return the majority element.
#The element appears more than n/2 times.

nums = [1, 3, 1, 3, 1]
#Output: 1

# first we gotta find out the frequerncy of each number 
# so are gonna find the freq
# first create empty count dict
# then use loop to find the freq
# the use another for loop to see find the majority


def majority_element(nums):

    count = {}

    for number in nums:
        if number in count:
            count[number] +=1
        else:
            count[number] = 1
    
    for number, freq in count.items():
        if freq > len(nums) / 2:
             return number
    return -1
print(majority_element(nums))


    