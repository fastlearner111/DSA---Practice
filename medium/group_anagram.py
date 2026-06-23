#Given an array of strings, group all anagrams together. 
#Return the groups in any order.

strs = ["eat","tea","tan","ate","nat","bat"]
#Output: [["eat","tea","ate"],["tan","nat"],["bat"]]
#
#Input:  strs = [""]
#Output: [[""]]
#
#Input:  strs = ["a"]
#Output: [["a"]]

def group_angram(strs):
    result = {}

    for s in strs:
        key = tuple(sorted(s))
        if key not in result:
            result[key] = []
        result[key]. append(s)
    return list(result.values())
print(group_angram(strs))          # time On(n * k), space : O(n)