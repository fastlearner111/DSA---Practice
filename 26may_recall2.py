#Next problem. Sliding Window Fixed.
nums = [2, 1, 5, 1, 3, 2]
k = 3
#Find maximum sum of any k consecutive elements.

# for this one we need two variable, one for current_window, and the othet for max_sum
# then we find the current window
# then we update the max_sum
# then we start the sliding window loop
# in that we find the current_window
# then we update the max_sum
# then we return the max_sum
# then print

def maximum_sum(nums, k):
    current_window = sum(nums[0:k])
    max_sum = current_window

    for i in range(k, len(nums)):
        current_window = current_window - nums[i-k] + nums[i]
        max_sum = max(current_window, max_sum)
    return max_sum
print(maximum_sum(nums,k))