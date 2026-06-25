#Given string s and integer k, replace at most k characters.
#Return length of longest substring with all same letters.
#
s = "ABAB"
k = 2
#Output: 4
#
#Input:  s = "AABABBA", k = 1
#Output: 4

def islongest(s,k):
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
print(islongest(s,k))