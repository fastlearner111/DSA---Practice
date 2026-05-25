nums = [2, 7, 11, 15] 
target = 9

#since we are looking for the index we are gonna use the index and number loop
# so first we create a empty dict with a variable name seen
# then we use the for loop
#inside that we are gonna find the complment
# then we are gonna see if that complement is in seen or not
# if yes then we return the the complement number and index
# else we update the index number and move to the next one and return nothing

def two_sum(nums,target):
 seen = {}

 for index, number in enumerate(nums):
  complement = target - number
  if complement in seen:
   return[seen[complement], index]
  
  else:
   seen[number] = index
 return []
print(two_sum(nums,target))