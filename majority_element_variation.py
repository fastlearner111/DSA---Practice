#Given an array, return True if a majority element exists 
#(appears more than n/2 times), False otherwise.

nums = [1, 2, 3, 4]
#Output: False

#Input:  nums = [2, 2, 1, 2]
#Output: True

# we are gonna first count which number has how many r3epitition using dict
# first creta a count empty dict
# find the frequency of each number then
# then use for loop to check if the number is greter than n/2
# if yes return True 
# else False

def majority_element(nums):
    count = {}

    for number in nums:
        if number in count:
            count[number] += 1
        else:
            count[number] = 1
    
    for number, freq in count.items():
        if freq > len(nums) / 2:
            return True
    return False
print(majority_element(nums))