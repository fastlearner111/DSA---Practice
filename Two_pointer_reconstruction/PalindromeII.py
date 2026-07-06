#Given a string s, return True if it can become a palindrome 
#by removing at most one character.
#
s = "aba"
#Output: True
#
#Input:  s = "abca"
#Output: True  (remove 'c' → "aba")
#
#Input:  s = "abc"
#Output: False

# Pattern - Two Pointr
# Data Structure = Two Pointer
# Approach = 
# Big O - On, On,

def isPalindrome(s,left,right):
    while left < right:
        if s[left] != s[right]:
            return False
        
        left += 1
        right -= 1
    return True

def validPalindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            skip_left = isPalindrome(s,left + 1, right)
            skip_right = isPalindrome(s, left, right - 1)
            return skip_left or skip_right
        
        left += 1
        right -= 1
    return True
print(validPalindrome(s))