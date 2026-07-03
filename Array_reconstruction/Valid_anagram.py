#Given two strings s and t, return True if t is an anagram of s.
#An anagram uses the same letters with the same frequency.
#
s = "anagram"
t = "nagaram"
#Output: True
#
#Input:  s = "rat", t = "car"
#Output: False

# Pattern - frequency and hash
# Data Structure  - dict
# approach -  we need to first check the frequncy for each s and t
# then sfter that we need see if count1 is equal to count2, if yes then return True
# else False
# On, On

def valid_anagram(s,t):
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
print(valid_anagram(s,t))