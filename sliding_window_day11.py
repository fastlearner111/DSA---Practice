nums = [2, 1, 5, 1, 3, 2]
k = 3

#first create a function then for this problem
# we need one current_window variable, one max_sum,
# so first we find the sum, so we do this by current_window = sum(nums[0:k])
# then we are say that the current_window is equal to the max_sum,which means max_sum updated
# then we use loop for range ,so that means we need to go right , and leave old element and new element
# inside the loop the current_window will be current_window- leaving_element + entering_element
#then again update the max_sum inside the loop using max
#then return max_sum
#then print


def slide_window(nums,k):

 current_window = sum(nums[0:k])
 max_sum = current_window
 for i in range(k, len(nums)):
  current_window = current_window - nums[i-k] +nums[i]
  max_sum = max(max_sum,current_window)
 return max_sum
print(slide_window(nums,k))
