##Given two strings s and t, return true if t is an anagram of s,
#and false otherwise.

s = "anagram"
t = "nagaram"
#Output: True
#
#Input:  s = "rat", t = "car"
#Output: False

def check_anagram(s,t):
    count1 = {}
    count2 = {}

    for char in s:
        if char in count1:
            count1[char] += 1
        else:
            count1[char] = 1
    for char in t:
        if char in count2:
            count2[char] += 1
        else:
            count2[char] = 1
    if count1 == count2:
        return True
    return False
print(check_anagram(s,t))