#Given an array of strings, group all anagrams together.
#Return the groups in any order.
#Do NOT use sorting. Use character frequency as the key.

strs = ["eat","tea","tan","ate","nat","bat"]
#Output: [["eat","tea","ate"],["tan","nat"],["bat"]]
#
#Input:  strs = [""]
#Output: [[""]]
#
#Input:  strs = ["a"]
#Output: [["a"]]
#
#Constraint: key must be built from character counts, not sorted string.

def group_anagram(strs):
    result = {}
    

    for s in strs:
     count = [0] * 26
     for c  in s:
      count[ord(c) - ord('a')] += 1
     key = tuple(count)
    
     if key not in result:
        result[key] = []
     result[key].append(s)

    return list(result.values())
print(group_anagram(strs)) 