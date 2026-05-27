#Given two strings, return True if they are anagrams of each other, False if not.
s1 = "listen"
s2 = "silent"
#Output: True

#Input: s1 = "hello", s2 = "world"
#Output: False

# we need two variabrle first is count1 for s1 and count2 for s2
# then we are gonna use loop fot s1, and then for s2,
# if the number is in count1 for s1, then count goes up by one, else it remians as it is
# same for s2,
# then we are gonna check if count1 and count2  are equal if yes then true else false



def check_anagram(s1,s2):
    count1 = {}
    count2 = {}

    for char in s1:
        if char in count1:
            count1[char] += 1
        else:
            count1[char] = 1

    for char in s2:
        if char in count2:
            count2[char] += 1
        else:
            count2[char] = 1
    
    if count1 == count2:
        return True
    
    return False
print(check_anagram(s1,s2))