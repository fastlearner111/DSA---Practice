#Write a function to find the longest common prefix string
#amongst an array of strings. If there is no common prefix,
#return an empty string "".

strs = ["flower","flow","flight"]
#Output: "fl"
#
#Input:  strs = ["dog","racecar","car"]
#Output: ""


def check_prefix(strs):
    prefix = ""

    for i in range(len(strs[0])):
        for nums in strs:
         if i >= len(nums) or  nums[i] != strs[0][i]:
                return prefix
        prefix += strs[0][i]
    return prefix
print(check_prefix(strs))
