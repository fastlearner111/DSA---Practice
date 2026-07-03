#Given an array of strings, group all anagrams together.
#Return the groups in any order.
#
strs = ["eat","tea","tan","ate","nat","bat"]
#Output: [["eat","tea","ate"],["tan","nat"],["bat"]]
#
#Input:  strs = [""]
#Output: [[""]]
#
#Input:  strs = ["a"]
#Output: [["a"]]

# Pattern - Hash and Frequency
# Data Structure -  dict
# Approach -  we need to sort the element and then we need to
# check if it matches the key or not , if yes then return the result
# Big O, -- On, On,

def group_anagram(strs):
    result = {}

    for char in strs:
        key = tuple(sorted(char))
        if key not in result:
            result[key] = []
        result[key].append(char)
    return list(result.values())
print(group_anagram(strs))