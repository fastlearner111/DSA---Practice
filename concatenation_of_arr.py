#Given an integer array nums of length n, return an array 
#of length 2n where the array is nums concatenated with 
#itself.

nums = [1, 2, 3]
#Output: [1, 2, 3, 1, 2, 3]

#Input:  nums = [1, 3, 2, 1]
#Output: [1, 3, 2, 1, 1, 3, 2, 1]

def concatenation_array(nums):

   

   ans = nums + nums
   return ans

print(concatenation_array(nums))