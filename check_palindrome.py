#A phrase is a palindrome if, after converting all uppercase 
#etters to lowercase and removing all non-alphanumeric 
#characters, it reads the same forward and backward.

s = "A man, a plan, a canal: Panama"
#Output: True

#@s = "raceacar"
#Output: False

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