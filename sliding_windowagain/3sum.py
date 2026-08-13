#Given an integer array nums, return 
#all the triplets [nums[i], nums[j], 
#nums[k]] where nums[i] + nums[j] + 
#nums[k] == 0, and the indices i, j 
#and k are all distinct.
#
#The output should not contain any 
#duplicate triplets. You may return 
#the output and the triplets in any
#order.
#
#Example 1:
nums = [-1,0,1,2,-1,-4]
#Output: [[-1,-1,2],[-1,0,1]]

def threesum(nums):
    new = sorted(nums)
    result = []

    for i in range(len(new)):
        if i > 0 and new[i] == new[i - 1]:
            continue

        left = i + 1
        right = len(new) - 1

        while left < right:
            if new[i] + new[left] + new[right] == 0:
                result.append([new[i],new[left],new[right]])
                left += 1

                while left < right and new[left] == new[left - 1]:
                    left += 1
            elif new[i] + new[left] + new[right] > 0:
                right -= 1
            else:
                left += 1
    return result
print(threesum(nums))
