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

    for char in strs: # we loop this until the list of strig is over
        key = tuple(sorted(char)) # we sort the char, sorting gives the answer in list and we want the answer in set so wrap it in tuple
        if key not in result: # if the sorted value i.e key not in result 
            result[key] = [] #then the key is empty
        result[key].append(char) # we append those value into those empty list
    return list(result.values()) # and then return the values in list
print(group_anagram(strs))