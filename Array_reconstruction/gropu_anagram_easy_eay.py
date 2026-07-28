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

from collections import defaultdict

def group_anagrams(strs):
    groups = defaultdict(list)

    for word in strs:
        sorted_word = ''.join(sorted(word))

        groups[sorted_word].append(word)

    return list(groups.values())
print(group_anagrams(strs))