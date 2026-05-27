#Given a sorted array of integers and a target,
#return the 1-based indices of the two numbers that add up to the target.
#Assume exactly one solution exists.
nums = [2, 7, 11, 15]
target = 9
#Output: [1, 2]

# so since the array is sorted, we use two pointer
# we need left and right variable, and also a current_sum variable
# we use while loop fot two pointer, and inside the loop
# we first calculate the current_sum
# then we use if statement to find whether the current_sum > target, or less than , or equal
# then accordingly we move our pointer
# then print

def check_indices(nums, target):
    left = 0
    right = len(nums) - 1
    

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return [left + 1 , right + 1]
        if current_sum > target:
            right -= 1
        if current_sum < target:
            left +=1
    return []
print(check_indices(nums,target))
