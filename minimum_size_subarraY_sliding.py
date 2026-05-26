#day 11

nums = [2, 3, 1, 2, 4, 3]
target = 7
#Output: 2  ([4, 3] has sum 7 with length 2)

# in the previous problem there used to be a order, we used to start from index 0 and move one step at a time
# but for this one the sum of index 0 and index 4 can also be the targted value
#soooo traverse doesnt work so maybe take one number and sum that that witht the remianing numbes,
#  no its gonna be too slow, so but the order for this problem is already as we wanted so we 
# start from index 0, the current_sum = sum(nums[0:1]), then we remove the left value and add right value, then 
# do the sum again like that until we reach the end index, and also we need to do from the back, damn to long and slow 

def min_size(nums,target):
  current_sum = 0
  left = 0
  min_length = float('inf')

  for right in range(len(nums)):
    current_sum += (nums[right])
    while current_sum >= target:
     min_length = min(min_length, right - left+1)
     current_sum -= nums[left]
     left += 1
  return min_length
print(min_size(nums,target))