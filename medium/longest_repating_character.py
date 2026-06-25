#You are given a string s and an integer k. You can replace at most k 
#characters in the string. Return the length of the longest substring 
#containing the same letter after the replacements.
#
s = "ABAB"
k = 2
#Output: 4
#
#Input:  s = "AABABBA", k = 1
#Output: 4

def isReplacement(s,k):
    seen = {}
    left = 0
    result = 0

    for right in range(len(s)):
        seen[s[right]] = seen.get(s[right], 0) + 1
        if (right - left + 1) - max(seen.values()) > k:
            seen[s[left]] -= 1
            left += 1
        result = max(result, right - left + 1)
    return result
print(isReplacement(s,k))