#Given an array of integers, return the majority element.
#The element appears more than n/2 times.

nums = [6, 5, 5, 6, 5, 6, 6, 6]
#Output: 6

# alright, first i need a empty dict
# then we are gonna find the frequency
# then we are gonna use another loop to find the majority
# compart with len(nums) / 2
# then retun it

def majority_element(nums):
    count = {}

    for number in nums:
        if number in count:
            count[number] += 1
        else:
            count[number] = 1
    
    for number, freq in count.items():
        if freq > len(nums) / 2:
         return number
    return -1
print(majority_element(nums))

    
    