#Given two strings s and t, return True if t is an anagram of s.
#An anagram uses the same letters with the same frequency.
#
s = "anagram"
t = "nagaram"
#Output: True
#
#Input:  s = "rat", t = "car"
#Output: False

def is_anagram(s,t):
    if len(s) != len(t):
        return False

    count = {}

    for char in s:
        if char not in count:
            count[char] = 0
        count[char] += 1

    for char in t:
        if char not in count:
            return False
        count[char] -= 1

        if count[char] <0:
            return False

    return True
print(is_anagram(s,t))

