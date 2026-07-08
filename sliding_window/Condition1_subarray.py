#Subarray With At Most K Distinct Integers

nums = [1,2,1,2,3]
k = 2
#Output: 12
#Explanation:
#The subarrays with at most 2 distinct integers are:
#[1], [2], [1], [2], [3],
#[1,2], [2,1], [1,2], [2,3],
#[1,2,1], [2,1,2]
#Total = 10

from collections import Counter

def atMostKdistict(nums,k):
    left = 0
    total = 0
    count = Counter()

    for right in range(len(nums)):
        count[nums[right]] += 1

        # shrink window until window has at most k distinct
        while len(count) > k:
            count[nums[left]] -= 1
            if count[nums[left]] == 0:
                del count[nums[left]]
            left += 1
        
        # all subarray ending at right are valid
        total += right - left + 1
    return total
print(atMostKdistict(nums,k))