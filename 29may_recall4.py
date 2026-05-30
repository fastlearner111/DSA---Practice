#Given two strings, return true if one is an anagram 
#of the other using a single dictionary.

s = "cinema"
t = "iceman"
#Output: True

def check_anagram(s,t):
    
    count1 = {}
    

    for char in s:
        if char in count1:
            count1[char] += 1
        else:
            count1[char] = 1
    for char in t:
        if char in count1:
         count1[char] -= 1
        else:
         count1[char] = -1
    
    if all(value == 0 for value in count1.values()):
       return True
    return False
print(check_anagram(s,t))

