#Given string s, find length of longest substring without repeating characters.
#
s = "abcabcbb"
#Output: 3
#
#Input:  s = "bbbbb"
#Output: 1

def islongest(s):
    subSet = set()
    result = 0
    left = 0

    for right in range(len(s)):
        while s[right] in subSet:
            subSet.remove(s[left])
            left += 1
        subSet.add(s[right])
        result = max(result, right - left + 1)
    return result
print(islongest(s))
        