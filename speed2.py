#Given a string s, return true if it is a valid 
#palindrome after removing non-alphanumeric characters 
#and converting to lowercase.

s = "A man, a plan, a canal: Panama"
#Output: True

def check_palindrome(s):

    cleaned  = [c.lower() for c in s if c.isalnum()]
    left = 0
    right = len(cleaned) - 1

    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        
        left += 1
        right -= 1
    return True
print(check_palindrome(s))
    