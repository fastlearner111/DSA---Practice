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

# pattern - freqeuncy and hash map
# data structure = maybe dict
# approach - so we need to seperate the like ones, 
# for that we need to sort then compare and see if that element is in the data structure


def group_anagram(strs):
    seen = {}

    for char in strs:
        key = tuple(sorted(char))
        if key not in seen:
            seen[key] = []
        seen[key].append(char)
    return list(seen.values())
print(group_anagram(strs))