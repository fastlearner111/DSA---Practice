#Given an array of strings, group all anagrams together.
#Return the groups in any order.
#
strs = ["eat","tea","tan","ate","nat","bat"]
#Output: [["eat","tea","ate"],["tan","nat"],["bat"]]
#
#Input:  strs = [""]
#Output: [[""]]

# so i am thinking of , we need to sort all then we need to compare and then store that into the result
# or maybe i can break the into small one, and do the operations there and do the sorting
# then write it like a output
# 

def group_anagram(strs):

    result = {}

    for s in strs:
        key = tuple(sorted(s))
        if key not in result:
            result[key] = []
        result[key]. append(s)
    return list(result.values())
print(group_anagram(strs))