#Given a string s, return True if it is a palindrome.
#Only alphanumeric characters count. Case insensitive.
#
s = "A man, a plan, a canal: Panama"
#Output: True
#
#Input:  s = "race a car"
#Output: False
#
#Input:  s = " "
#Output: True

# Pattern - Two Pointer
# Data Struccture - Two pointer
# Approach - First we need to check the first element and last element
# then if they are not equal then false, else true 
# Big O -On, On, 

def check_palindrome(s):
    cleaned = [c.lower() for c in s if c.isalnum()]
    left = 0
    right = len(cleaned) - 1

    while left < right:
        if cleaned[left] != cleaned[right]:
            return False

        left += 1
        right -= 1
    return True
print(check_palindrome(s)) 