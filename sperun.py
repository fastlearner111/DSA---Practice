#Given an array of strings strs, return the longest common prefix.
#If there is no common prefix, return "".
#
strs = ["flower","flow","flight"]
#Output: "fl"
#
#Input:  strs = ["dog","racecar","car"]
#Output: ""

def longest_prefix(strs):
    prefix = ""

    for i in range(len(strs[0])):
        for num in strs:
            if  i >= len(num) or num[i] != strs[0][i]:
                return prefix
        prefix += strs[0][i]
    return prefix
print(longest_prefix(strs))