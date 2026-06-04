#Given an integer array nums and an integer k, return 
#the count of pairs where nums[i] == nums[j] and 
#abs(i - j) <= k.

nums = [1,2,3,1,1]
k = 2
#Output: 2

def check_duplicate(nums,k):
     seen = {}
     count = 0

     for i, number in enumerate(nums):
          if number in seen:
               if abs(i - seen[number]) <= k:
                count += 1
                seen[number] = i
               else:
                seen[number] = i
          else:
             seen[number] = i
           
     return count
print(check_duplicate(nums,k))
