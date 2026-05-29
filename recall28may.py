#Given an array of integers and a window size k, 
#return the maximum sum of any k consecutive elements.

nums = [2, 3, 4, 1, 5]
k = 2
#Output: 7


def slide_window(nums, k):

    current_window = sum(nums[0:k])
    max_sum = current_window

    for n in range(k, len(nums)):
        current_window = current_window - nums[n-k] + nums[n]
        max_sum = max(current_window, max_sum)

    return max_sum
print(slide_window(nums,k))