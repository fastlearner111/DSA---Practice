#Given a string s, find the length of the longest substring 
#without repeating characters.
#
s = "abcabcbb"
#Output: 3  (substring "abc")
#
#Input:  s = "bbbbb"
#Output: 1  (substring "b")
#
#Input:  s = "pwwkew"
#Output: 3  (substring "wke")
#
#Input:  s = ""
#Output: 0

def longest_substring(s):
    left = 0
    charSet = set()
    result = 0

    for right in range(len(s)):
        while s[right] in charSet:
            charSet.remove(s[left])
            left += 1
        charSet.add(s[right])
        result = max(result, right - left + 1)
    return result
print(longest_substring(s))