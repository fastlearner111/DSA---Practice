#Given a string s, return true if it is a palindrome 
#after removing non-alphanumeric characters and 
#converting to lowercase.

s = "Was it a car or a cat I saw?"
#utput: True

def check_palindrome(s):

    cleaned = [c.lower() for c in s if c.isalnum()]
    left = 0
    right = len(cleaned) - 1

    while left < right:
        if cleaned[left] != cleaned[left]:
            return False
        left += 1
        right -= 1
    return True
print(check_palindrome(s))