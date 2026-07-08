s = "abcabcbb"
#Output: 3
#Explanation: "abc" is the longest substring without repeating characters.
#
#Input: s = "bbbbb"
#Output: 1
#Explanation: "b" is the longest substring without repeating characters.
#
#Input: s = "pwwkew"
#Output: 3
#Explanation: "wke" is the longest substring without repeating characters.

# Condition 1 = duplicate inside window  
#Invalid window = s[right] in window

def longestSub(s):
    left = 0
    window = set()
    longest = 0

    for right in range(len(s)):
        # shrink until window has no duplicate
        while s[right] in window:
            window.remove(s[left])
            left += 1
        
        # expand window
        window.add(s[right])

        # update answer
        longest = max(longest, right - left + 1)
    return longest
print(longestSub(s))

